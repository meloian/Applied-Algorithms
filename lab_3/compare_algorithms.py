import sys
import os
import time
import random
import statistics
import matplotlib.pyplot as plt

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../lab_2')))

from undirected_graph import UndirectedGraph
from shortest_paths import PathFinder

def generate_graph(n, p):

    graph = UndirectedGraph(n)
    graph.generate_random_graph(p)
    return graph 

def measure_dijkstra(graph):
    graph.matrix_to_list()
    sp = PathFinder(graph)
    
    total_time = 0

    for i in range(100):
        start_time = time.perf_counter()
        sp.all_pairs_dijkstra()
        end_time = time.perf_counter()

        iteration_time = end_time - start_time
        total_time += iteration_time

    average_time = total_time / 100
    return average_time

def measure_floyd_warshall(graph):

    if graph.rep != 'matrix':
        graph.list_to_matrix()
    sp = PathFinder(graph)

    total_time = 0

    for i in range(100):
        start_time = time.perf_counter()
        sp.floyd_warshall()
        end_time = time.perf_counter()

        iteration_time = end_time - start_time
        total_time += iteration_time

    average_time = total_time / 100 
    return average_time

if __name__ == "__main__":
    
    print(f"{'n':<6}{'p':<10}{'Dijkstra (sec)':<20}{'Floyd-Warshall (sec)':<20}")
    
    n_values = []
    p_values = []
    dijkstra_times = []
    floyd_warshall_times = []
    
    for n in [5, 10, 20, 50, 100]:
        for p in [0.1, 0.25, 0.5]:
            graph = generate_graph(n, p)

            dijkstra_time = measure_dijkstra(graph)
            floyd_warshall_time = measure_floyd_warshall(graph)

            n_values.append(n)
            p_values.append(p)
            dijkstra_times.append(dijkstra_time)
            floyd_warshall_times.append(floyd_warshall_time)

            print(f"{n:<6}{p:<10}{dijkstra_time:<20}{floyd_warshall_time:<20}")

    plt.figure(figsize=(10, 6))
    plt.plot(n_values, dijkstra_times, label='Dijkstra', linestyle='-', marker='')
    plt.plot(n_values, floyd_warshall_times, label='Floyd-Warshall', linestyle='-', marker='')

    plt.xlabel('Number of Vertices (n)')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Comparison of Dijkstra and Floyd-Warshall Algorithms')
    plt.legend()
    plt.grid(True)

    plt.show()