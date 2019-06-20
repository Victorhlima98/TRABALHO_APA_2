import utils


def main(x, y):

    s = utils.get_random_list(x, 0, y)
    f = utils.get_random_list(x, 0, y)

    assert(len(s) == len(f))
    n = len(s)
    a = []
    k = 0
    for m in range(1, n):
        if s[m] >= f[k]:
            a.append(m)
            k = m
    return a
