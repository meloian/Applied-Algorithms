import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../lab_2')))

from undirected_graph import UndirectedGraph
from shortest_paths import PathFinder

if __name__ == "__main__":
    print("Undirected graph with weights:")
    graph = UndirectedGraph(4)
    graph.add_edge(0, 1, 2)
    graph.add_edge(0, 2, 5)
    graph.add_edge(1, 2, 1)
    graph.add_edge(2, 3, 3)
    graph.display_matrix()

    graph.matrix_to_list()

    sp = PathFinder(graph)

    print("\nShortest paths using Dijkstra's algorithm (from each vertex):")
    dijkstra_paths = sp.all_pairs_dijkstra()
    for vertex, paths in dijkstra_paths.items():
        print(f"\nFrom vertex {vertex}:")
        for target, distance in paths.items():
            print(f"  To vertex {target}: distance = {distance}")

    graph.list_to_matrix()

    print("\nShortest paths using Floyd-Warshall algorithm (distance matrix):")
    floyd_warshall_paths = sp.floyd_warshall()

    print("\nDistance matrix (rows represent start vertices, columns represent target vertices):")
    header = "    " + "  ".join([f"{i:2}" for i in range(graph.n)])
    print(header)
    print("  " + "-" * (len(header) + 1))
    for i, row in enumerate(floyd_warshall_paths):
        row_str = "  ".join([f"{dist:2}" if dist != sp.INF else "∞ " for dist in row])
        print(f"{i:2} | {row_str}") 