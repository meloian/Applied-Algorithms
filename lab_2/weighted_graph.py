import random
from graph import Graph

class WeightedGraph(Graph):
    def add_vertex(self):
        self.n += 1
        if self.rep == 'matrix':
            for row in self.matrix:
                row.append(0)
            self.matrix.append([0] * self.n)
        elif self.rep == 'list':
            self.neighbors[self.n - 1] = []

    def add_edge(self, v1, v2, weight=1):
        # add a weighted edge between v1 and v2
        if v1 >= self.n or v2 >= self.n:
            return
        if self.rep == 'matrix':
            # update the matrix with the weight
            if not self.has_edge(v1, v2):
                self.matrix[v1][v2] = weight
                self.matrix[v2][v1] = weight
        elif self.rep == 'list':
            if v2 not in [edge[0] for edge in self.neighbors[v1]]:
                self.neighbors[v1].append((v2, weight))
                self.neighbors[v2].append((v1, weight))

    def remove_vertex(self, v):
        # remove a vertex and all its edges
        if v >= self.n:
            return
        if self.rep == 'matrix':
            self.matrix.pop(v)
            for row in self.matrix:
                row.pop(v)
        elif self.rep == 'list':
            del self.neighbors[v]
            for key in list(self.neighbors.keys()):
                self.neighbors[key] = [edge for edge in self.neighbors[key] if edge[0] != v]
        self.n -= 1

    def remove_edge(self, v1, v2):
        if v1 >= self.n or v2 >= self.n:
            return
        if self.rep == 'matrix':
            # set the edge weight to 0 in the matrix
            self.matrix[v1][v2] = 0
            self.matrix[v2][v1] = 0
        elif self.rep == 'list':
            self.neighbors[v1] = [edge for edge in self.neighbors[v1] if edge[0] != v2]
            self.neighbors[v2] = [edge for edge in self.neighbors[v2] if edge[0] != v1]

    def generate_random_weighted_graph(self, p, weight_range=(1, 10)):
        # generate a random weighted graph using Erdős–Rényi model
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if random.random() < p:
                    weight = random.randint(*weight_range)  # random weight in the given range
                    self.add_edge(i, j, weight) 