import random
from graph import Graph

class DirectedGraph(Graph):
    def add_vertex(self):
        self.n += 1
        if self.rep == 'matrix':
            for row in self.matrix:
                row += [0]
            self.matrix.append([0] * self.n)
        elif self.rep == 'list':
            self.neighbors[self.n - 1] = []

    def add_edge(self, v1, v2, weight=1):
        # add a directed edge (v1 -> v2)
        if v1 < self.n and v2 < self.n:
            if self.rep == 'matrix':
                if not self.has_edge(v1, v2):
                    self.matrix[v1][v2] = weight
            elif self.rep == 'list':
                if v2 not in [edge[0] for edge in self.neighbors[v1]]:
                    self.neighbors[v1].append((v2, weight))

    def remove_vertex(self, v):
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
        # remove directed edge (v1 -> v2)
        if v1 >= self.n or v2 >= self.n:
            return
        if self.rep == 'matrix':
            self.matrix[v1][v2] = 0
        elif self.rep == 'list':
            self.neighbors[v1] = [edge for edge in self.neighbors[v1] if edge[0] != v2]

    def generate_random_directed_graph(self, p):
        for i in range(self.n):
            for j in range(self.n):
                if i != j and random.random() < p:
                    self.add_edge(i, j) 