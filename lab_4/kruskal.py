from unionfind import UnionFind

class KruskalMST:
    def __init__(self, vertices):
        self.V = vertices  # number of vertices
        self.E = []  # list of edges

    def add_edge(self, u, v, w):
        self.E.append((u, v, w))

    def find_mst(self):
        
        self.E.sort(key=lambda edge: edge[2])
        disjoint_sets = UnionFind(self.V)
        
        mst = []
        total_weight = 0
        
        for (u, v, w) in self.E:
            # if vertices are in different sets, add edge to MST
            if disjoint_sets.find(u) != disjoint_sets.find(v):
                disjoint_sets.union(u, v)
                mst.append((u, v, w))
                total_weight += w
        
        return mst, total_weight 