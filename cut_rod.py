import time
import utils

def main(p, n):
    if n == 0:
        return 0
    q = float('-inf')
    for i in range(1, n+1):
        q = max(q, p[i] + main(p, n-i))
    return q


def cut_rod_pd(p, n, r):
    if n in r.keys():
        return r[n]
    if n==0:
        return n
    else:
        q = float('-inf')
        for i in range(1, n+1):
            q = max(q, p[i] + cut_rod_pd(p, n-i, r))
    r[n] = q
    return q

def mai_n():
    x = 20
    p = utils.get_random_list(x + 1)
    t1 = time.time()
    print("cut_rod: ", cut_rod(p, x))
    t2 = time.time()
    print("cut_rod_pd: ", cut_rod_pd(p, x, {}))
    t3 = time.time()
    print("tempo cut_rod: ", (t2 - t1))
    print("tempo cut_rod_pd: ", (t3 - t2))


if __name__ == '__main__':
    main()