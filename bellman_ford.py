from collections import defaultdict


def main(edges, source):
    g = defaultdict(list)
    for l, r, c in edges:
        g[l].append((r, c))

    graph = {}
    for gl in g:
        sla = {}
        for c in g[gl]:
            if g[gl] == [(None, None)]:
                graph.update({gl: {}})
            else:
                sla.update({c[0]: c[1]})
                graph.update({gl: sla})

    distance, predecessor = dict(), dict()
    for node in graph:
        distance[node], predecessor[node] = float('inf'), None
    distance[source] = 0

    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbour in graph[node]:
                # If the distance between the node and the neighbour is lower than the current, store it
                if distance[neighbour] > distance[node] + graph[node][neighbour]:
                    distance[neighbour], predecessor[neighbour] = distance[node] + graph[node][neighbour], node

    for node in graph:
        for neighbour in graph[node]:
            assert distance[neighbour] <= distance[node] + graph[node][neighbour], "Negative weight cycle."

    return distance, predecessor


if __name__ == '__main__':
    edges = [
        ("A", "B", 7),
        ("A", "D", 5),
        ("B", "C", 8),
        ("B", "D", 9),
        ("B", "E", 7),
        ("C", "E", 5),
        ("D", "E", 15),
        ("D", "F", 6),
        ("E", "F", 8),
        ("E", "G", 9),
        ("F", "G", 11),
        ("G", "F", 50)
    ]

    distance, predecessor = main(edges, source='A')

    print(distance)