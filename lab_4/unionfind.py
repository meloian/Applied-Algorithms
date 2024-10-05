class UnionFind:
    def __init__(self, n):
        self.R = list(range(n))
        self.List = list(range(n))
        self.Next = [-1] * n  # next element, -1 means end
        # self.Next = [0] * n  # used 0 as end (changed to avoid cycles)
        self.Size = [1] * n
        self.internal_names = list(range(n))
        self.external_names = list(range(n))

    def find(self, x):
        if x != self.R[x]:
            self.R[x] = self.find(self.R[x])
        return self.R[x]
        # return self.external_names[self.R[x]] - without compression

    def union(self, x, y):
        A = self.find(self.internal_names[x])
        B = self.find(self.internal_names[y])

        if A == B:
            return

        # make A the smaller set
        if self.Size[A] > self.Size[B]:
            A, B = B, A

        # update roots for all elements in set A
        z = self.List[A]
        last = None
        while z != -1:  # changed from 0 to -1 to avoid cycles
            self.R[z] = B
            last = z
            z = self.Next[z]
        # while z != 0:  # previous used 0 as end (changed to avoid cycles)
        #     self.R[z] = B
        #     last = z
        #     z = self.Next[z]

        # link last element of A to first of B
        if last is not None:
            self.Next[last] = self.List[B]

        # update List and Size for set B
        if self.List[A] != -1:
            self.List[B] = self.List[A]
        self.Size[B] += self.Size[A]

        # update names to reflect new root
        self.internal_names[x] = B
        self.external_names[B] = x 