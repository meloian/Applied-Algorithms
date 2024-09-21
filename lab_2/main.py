from undirected_graph import UndirectedGraph
from directed_graph import DirectedGraph
from weighted_graph import WeightedGraph
from visualizer_tk import GraphVisualizer

if __name__ == "__main__":
    print("Undirected graph:")
    undirected_graph = UndirectedGraph(4)
    undirected_graph.add_edge(0, 1)
    undirected_graph.add_edge(2, 3)
    undirected_graph.display_matrix()

    print("\nDirected graph:")
    directed_graph = DirectedGraph(4)
    directed_graph.add_edge(0, 1)
    directed_graph.add_edge(1, 2)
    directed_graph.display_matrix()

    print("\nWeighted graph:")
    weighted_graph = WeightedGraph(4)
    weighted_graph.add_edge(0, 1, 5)
    weighted_graph.add_edge(2, 3, 10)
    weighted_graph.display_matrix()

    print("\nConvert to adjacency list:")
    undirected_graph.matrix_to_list()
    undirected_graph.display_list()

    print("\nConvert back to matrix:")
    undirected_graph.list_to_matrix()
    undirected_graph.display_matrix()

    print("\nRandom undirected graph:")
    random_graph = UndirectedGraph(5)
    random_graph.generate_random_graph(0.5)
    random_graph.display_matrix()

    print("\nRandom directed graph:")
    random_directed_graph = DirectedGraph(5)
    random_directed_graph.generate_random_directed_graph(0.5)
    random_directed_graph.display_matrix()

    print("\nRandom weighted graph:")
    random_weighted_graph = WeightedGraph(5)
    random_weighted_graph.generate_random_weighted_graph(0.5, (1, 10))
    random_weighted_graph.display_matrix() 

    visualizer = GraphVisualizer(random_weighted_graph)
    visualizer.visualize()
    
    visualizer = GraphVisualizer(random_graph)
    visualizer.visualize()