import random
import time


def report_time(func, inp, n_iter=1):
    start = time.time()

    for i in range(n_iter):
        func.main(*inp)

    end = time.time()
    total_time = end - start
    print('Total time for %s after %d iterations: %f' % (func.__name__, n_iter, total_time))


def get_random_list(n, min_val=0, max_val=1000):
    return [random.randint(min_val, max_val) for _ in range(n)]


def get_random_int(min_val=0, max_val=1000):
    return random.randint(min_val, max_val)


def get_random_float(min_val=0, max_val=100):
    return random.uniform(min_val, max_val)


def gen_edges(n, l, x):
    edges = []
    vertices = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    for i in range(n):
        a = random.choice(vertices[:x])
        b = random.choice(vertices[:x])
        while a == b:
            b = random.choice(vertices[:x])
        edges.append((a, b, random.randint(1, l)))
    return edges


class WeightedGraph:
    def __init__(self, n, l, x):
        self.vertices = range(x)
        self.edges = []

        for i in range(n):
            a = random.choice(self.vertices[:x])
            b = random.choice(self.vertices[:x])
            while a == b:
                b = random.choice(self.vertices[:x])
            self.edges.append((random.randint(1, l), a, b))

        self.graph = [[0] * len(self.vertices) for _ in range(len(self.vertices))]

        for i in range(len(self.edges)):
            weight, u, v, = self.edges[i]
            self.graph[u][v] = weight
            self.graph[v][u] = weight