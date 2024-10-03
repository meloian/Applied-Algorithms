class PathFinder:
    def __init__(self, graph):
        self.graph = graph
        self.num_vertices = graph.n
        self.INF = float('inf')  # infinity value for unreachable paths

    def dijkstra(self, start):
        distances = {}
        for v in range(self.num_vertices):
            distances[v] = self.INF  # set all distances to infinity
        distances[start] = 0  # distance to start vertex is 0

        # initialize visited vertices
        visited = []
        for _ in range(self.num_vertices):
            visited.append(False)  # mark all vertices as unvisited

        # iterate to find shortest paths
        for _ in range(self.num_vertices):
            min_vertex = None
            for v in range(self.num_vertices):
                if not visited[v]:
                    if min_vertex is None:
                        min_vertex = v  # first unvisited vertex
                    elif distances[v] < distances[min_vertex]:
                        min_vertex = v  # update min vertex if a shorter distance is found

            # if no reachable vertices remain, exit
            if min_vertex is None:
                break
            if distances[min_vertex] == self.INF:
                break

            # mark the current vertex as visited
            visited[min_vertex] = True

            # update distances for neighbors of the current vertex
            for neighbor, weight in self.graph.neighbors[min_vertex]:
                if not visited[neighbor]:
                    new_dist = distances[min_vertex] + weight
                    if new_dist < distances[neighbor]:
                        distances[neighbor] = new_dist  # update if a shorter path is found

        return distances

    def floyd_warshall(self):
        dist_matrix = []
        
        for i in range(self.num_vertices):
            row = []
            for j in range(self.num_vertices):
                if i == j:
                    row.append(0)  # distance to itself is 0
                elif self.graph.matrix[i][j] != 0:
                    row.append(self.graph.matrix[i][j])  # use the edge weight if there is an edge
                else:
                    row.append(self.INF)  # if no edge, set distance to infinity
            dist_matrix.append(row)

        # Floyd-Warshall algorithm to find shortest paths
        k = 0
        while k < self.num_vertices:
            i = 0
            while i < self.num_vertices:
                j = 0
                while j < self.num_vertices:
                    # update the distance if a shorter path through vertex k is found
                    if dist_matrix[i][k] < self.INF and dist_matrix[k][j] < self.INF:
                        dist_matrix[i][j] = min(dist_matrix[i][j], dist_matrix[i][k] + dist_matrix[k][j])
                    j += 1
                i += 1
            k += 1

        return dist_matrix

    def all_pairs_dijkstra(self):
        all_distances = {}
        for start in range(self.num_vertices):
            all_distances[start] = self.dijkstra(start)
        return all_distances 