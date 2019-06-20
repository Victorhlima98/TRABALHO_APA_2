import bellman_ford
import cut_rod
import dijkstra
import selecao_atividades
import huffman
import kruskal
import mochila
import prim
import utils

if __name__ == '__main__':
    for n in [50, 100, 500, 1000, 5000, 10000, 15000]:
        print(n)
        WG = utils.WeightedGraph(n, 20, 5)
        utils.report_time(kruskal, [WG], n_iter=1)
        utils.report_time(prim, [WG], n_iter=1)
        print

        edges = utils.gen_edges(n, 20, 5)
        utils.report_time(bellman_ford, [edges, 'A'], n_iter=1)
        utils.report_time(dijkstra, [edges, 'A', 'E'], n_iter=1)
        print

        utils.report_time(selecao_atividades, [n, 10], n_iter=1)
        utils.report_time(huffman, [n], n_iter=1)
        print

        values = utils.get_random_list(n)
        weights = utils.get_random_list(n)
        utils.report_time(cut_rod, [values, 10], n_iter=1)
        utils.report_time(mochila, [values, weights, n, n], n_iter=1)
        print
