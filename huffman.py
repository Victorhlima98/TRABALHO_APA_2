import heapq
import random


def main(x):
    freqmap = {'a': 6.516, 'b': 1.886, 'c': 2.732, 'd': 5.076, 'e': 16.396, 'f': 1.656, 'g': 3.009, 'h': 4.577, 'i': 6.550,
               'j': 0.268, 'k': 1.417, 'l': 3.437, 'm': 2.534, 'n': 9.776, 'o': 2.594, 'p': 0.670, 'q': 0.018, 'r': 7.003,
               's': 7.270, 't': 6.154, 'u': 4.166, 'v': 0.846, 'w': 1.921, 'x': 0.034, 'y': 0.039, 'z': 1.134}
    huffman(freqmap)

    l = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    text = ""
    for _ in range(x):
        text += random.choice(l)
    char_to_code, encoded = huffman_encode(text)
    huffman_decode(invert_dictionary(char_to_code), encoded)


def huffman(freqmap):
    class Node:
        def __init__(self, freq, char, left=None, right=None):
            self.__left = left
            self.__right = right
            self.__freq = freq
            self.__char = char

        def addLeft(self, left):
            self.__left = left

        def addRight(self, right):
            self.__right = right

        def freq(self):
            return self.__freq

        def char(self):
            return self.__char

        def hasLeft(self):
            return self.__left is not None

        def hasRight(self):
            return self.__right is not None

        def isTerminal(self):
            return not (self.hasLeft()) and not (self.hasRight())

        def left(self):
            return self.__left

        def right(self):
            return self.__right

        def __lt__(self, other):
            return self.freq() < other.freq()

    queue = [Node(freq, key) for key, freq in freqmap.items()]
    heapq.heapify(queue)
    for i in range(len(freqmap) - 1):
        left_node = heapq.heappop(queue)
        right_node = heapq.heappop(queue)
        heapq.heappush(queue, Node(left_node.freq() + right_node.freq(), None, left_node, right_node))

    root = heapq.heappop(queue)

    # special case: freqmap with one element only
    if root.isTerminal():
        return {root.char(): '0'}

    stack = [(root, "")]
    char_to_code = {}
    while len(stack) > 0:
        node, code = stack.pop()
        if node.hasLeft():
            stack.append((node.left(), code + '0'))

        if node.hasRight():
            stack.append((node.right(), code + '1'))

        if node.isTerminal():
            char_to_code[node.char()] = code

    return dict(sorted(char_to_code.items()))  # sort the dict for better readability


def huffman_encode(text):
    def build_freqmap(text):
        length = len(text)
        freqmap = {}

        for i in text:
            freqmap[i] = freqmap.get(i, 0) + 1

        for key in freqmap.keys():
            freqmap[key] = (freqmap[key] / length) * 100

        return freqmap

    char_to_code = huffman(build_freqmap(text))
    encoded_symbols = []
    for x in text:
        encoded_symbols.append(char_to_code[x])
    return char_to_code, ''.join(encoded_symbols)


def huffman_decode(code_to_char, encoded):
    decoded_symbols = []
    symbol_start = 0
    symbol_end = 1
    length = len(encoded)
    while symbol_end <= length:
        key = encoded[symbol_start:symbol_end]
        if key in code_to_char:
            decoded_symbols.append(code_to_char[key])
            symbol_start = symbol_end
        else:
            symbol_end = symbol_end + 1

    if symbol_start < length:
        raise ValueError("The encoded string cannot be recognized")

    return ''.join(decoded_symbols)


def invert_dictionary(dictionary):
    return dict(map(reversed, dictionary.items()))
