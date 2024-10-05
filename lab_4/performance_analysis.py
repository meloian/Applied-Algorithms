import time
import random
import math
import sys
import os
import matplotlib.pyplot as plt

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../lab_2')))

from kruskal import KruskalMST
from weighted_graph import WeightedGraph

def measure_execution_time(num_vertices, edge_prob, iterations=100):
    total_time = 0.0

    for _ in range(iterations):
        graph = WeightedGraph(num_vertices)
        graph.generate_random_weighted_graph(p=edge_prob, weight_range=(1, 100))

        # convert graph for Kruskal's algorithm
        kruskal_graph = KruskalMST(graph.n)
        if graph.rep == 'matrix':
            for i in range(graph.n):
                for j in range(i + 1, graph.n):
                    if graph.matrix[i][j] != 0:
                        kruskal_graph.add_edge(i, j, graph.matrix[i][j])

        # time of Kruskal's algorithm
        start_time = time.time()
        kruskal_graph.find_mst()
        end_time = time.time()

        total_time += (end_time - start_time)

    return total_time / iterations

def theoretical_kruskal_time(vertices, edge_prob):
    edges = edge_prob * (vertices * (vertices - 1)) / 2
    return edges * math.log2(vertices)  # O(E log V)

def performance_comparison_with_text():
    num_vertices_list = [10, 20, 50, 100, 200, 500, 750, 1000]
    execution_times = []
    theoretical_times = []

    edge_prob = 0.7
    iterations = 100
    
    for num_vertices in num_vertices_list:
        # measure average execution time
        actual_time = measure_execution_time(num_vertices, edge_prob, iterations)
        execution_times.append(actual_time)

        # calculate theoretical time
        theoretical_time = theoretical_kruskal_time(num_vertices, edge_prob)
        theoretical_times.append(theoretical_time)

        print(f"Number of Vertices: {num_vertices}")
        print(f"Average Measured Execution Time: {actual_time:.6f} seconds")
        print(f"Theoretical Time (p={edge_prob}): {theoretical_time:.6f} (units)")
        print("-" * 40)

    # normalize theoretical data to actual
    normalization_factor = execution_times[0] / theoretical_times[0]
    normalized_theoretical_times = [time * normalization_factor for time in theoretical_times]

    plt.plot(num_vertices_list, execution_times, label="Measured Average Execution Time (seconds)", marker='o')
    plt.plot(num_vertices_list, normalized_theoretical_times, label="Normalized Theoretical Time (units)", marker='x')
    plt.xlabel('Number of Vertices')
    plt.ylabel('Time (seconds or normalized units)')
    plt.title(f'Kruskal Algorithm Performance Analysis (p={edge_prob}, Average of 100 Runs)')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    performance_comparison_with_text()