class UF:
    def __init__(self, N):
        self._id = [i for i in range(N)]

    def connected(self, p, q):
        return self._find(p) == self._find(q)

    def union(self, p, q):
        p_root = self._find(p)
        q_root = self._find(q)
        if p_root == q_root:
            return
        self._id[p_root] = q_root

    def _find(self, p):
        while p != self._id[p]:
            p = self._id[p]
        return p


def main(G):
    MST = set()
    edges = set()
    for j in range(len(G.vertices)):
        for k in range(len(G.vertices)):
            if G.graph[j][k] != 0 and (k, j) not in edges:
                edges.add((j, k))
    sorted_edges = sorted(edges, key=lambda e: G.graph[e[0]][e[1]])
    uf = UF(len(G.vertices))
    for e in sorted_edges:
        u, v = e
        if uf.connected(u, v):
            continue
        uf.union(u, v)
        MST.add(e)
    return MST