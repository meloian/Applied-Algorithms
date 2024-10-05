import sys
import os
import tkinter as tk

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../lab_2')))

from weighted_graph import WeightedGraph
from undirected_graph import UndirectedGraph
from visualizer_tk import GraphVisualizer
from kruskal import KruskalMST

if __name__ == "__main__":
    graph = WeightedGraph(5)
    graph.generate_random_weighted_graph(p=0.7, weight_range=(1, 10))

    graph.display_matrix()

    visualizer = GraphVisualizer(graph)
    visualizer.visualize()

    kruskal_graph = KruskalMST(graph.n)
    if graph.rep == 'matrix':
        for i in range(graph.n):
            for j in range(i + 1, graph.n):
                if graph.matrix[i][j] != 0:
                    kruskal_graph.add_edge(i, j, graph.matrix[i][j])

    mst, total_weight = kruskal_graph.find_mst()
    print("Edges in the Minimum Spanning Tree:")
    for u, v, weight in mst:
        print(f"{u} -- {v} == {weight}")

    mst_graph = UndirectedGraph(graph.n)
    mst_graph.rep = 'list'
    mst_graph.neighbors = {i: [] for i in range(graph.n)}
    for u, v, weight in mst:
        mst_graph.neighbors[u].append((v, weight))
        mst_graph.neighbors[v].append((u, weight))

    visualizer = GraphVisualizer(mst_graph)
    visualizer.visualize() 