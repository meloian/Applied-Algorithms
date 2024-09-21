import random
from graph import Graph

class UndirectedGraph(Graph):
    def add_vertex(self):
        # add a new vertex
        self.n += 1
        if self.rep == 'matrix':
            for row in self.matrix:
                row.append(0)  # expand each row
            self.matrix.append([0] * self.n)  # add new row
        elif self.rep == 'list':
            self.neighbors[self.n - 1] = []  # new empty list

    def add_edge(self, v1, v2, weight=1):
        # add edge between v1 and v2
        if v1 < self.n and v2 < self.n:
            if self.rep == 'matrix':
                if not self.has_edge(v1, v2):
                    self.matrix[v1][v2] = weight
                    self.matrix[v2][v1] = weight  # symmetry for undirected
            elif self.rep == 'list':
                if v2 not in [edge[0] for edge in self.neighbors[v1]]:
                    self.neighbors[v1].append((v2, weight))
                    self.neighbors[v2].append((v1, weight))  # symmetry

    def remove_vertex(self, v):
        # remove a vertex
        if v < self.n:
            if self.rep == 'matrix':
                self.matrix.pop(v)  # remove row
                for row in self.matrix:
                    row.pop(v)  # remove column
            elif self.rep == 'list':
                del self.neighbors[v]
                for key in list(self.neighbors):
                    self.neighbors[key] = [edge for edge in self.neighbors[key] if edge[0] != v]
            self.n -= 1

    def remove_edge(self, v1, v2):
        # remove edge between v1 and v2
        if v1 < self.n and v2 < self.n:
            if self.rep == 'matrix':
                self.matrix[v1][v2] = 0
                self.matrix[v2][v1] = 0
            elif self.rep == 'list':
                self.neighbors[v1] = [edge for edge in self.neighbors[v1] if edge[0] != v2]
                self.neighbors[v2] = [edge for edge in self.neighbors[v2] if edge[0] != v1]

    def generate_random_graph(self, p):
        # generate a random undirected graph using Erdős–Rényi model
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if random.random() < p:
                    self.add_edge(i, j)  