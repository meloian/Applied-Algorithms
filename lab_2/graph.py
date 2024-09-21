import random

class Graph:
    def __init__(self, n):
        # initialize graph with 'n' vertices, matrix representation
        self.n = n
        self.matrix = [[0] * n for _ in range(n)]
        self.neighbors = None
        self.rep = 'matrix'

    def has_edge(self, v1, v2):
        # check if edge exists between v1 and v2
        if self.rep == 'matrix':
            if v1 < self.n and v2 < self.n:
                return self.matrix[v1][v2] != 0
        print("Switch to matrix representation.")
        return False

    def matrix_to_list(self):
        # convert matrix to adjacency list
        if self.rep == 'matrix':
            self.neighbors = {i: [] for i in range(self.n)}
            for i in range(self.n):
                for j in range(self.n):
                    if self.matrix[i][j]:
                        self.neighbors[i].append((j, self.matrix[i][j]))
            self.matrix = None
            self.rep = 'list'

    def list_to_matrix(self):
        # convert adjacency list back to matrix
        if self.rep == 'list':
            self.matrix = [[0] * self.n for _ in range(self.n)]
            for i in self.neighbors:
                for j, weight in self.neighbors[i]:
                    self.matrix[i][j] = weight
            self.neighbors = None
            self.rep = 'matrix'

    def display_matrix(self):
        # display adjacency matrix
        if self.rep == 'matrix':
            for row in self.matrix:
                print(row)
        else:
            print("Matrix not available.")

    def display_list(self):
        # display adjacency list
        if self.rep == 'list':
            for vertex, edges in self.neighbors.items():
                print(f"{vertex}: {edges}")
        else:
            print("List not available.") 