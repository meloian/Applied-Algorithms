class SetOperations:
    def __init__(self):
        self.items = []

    def insert(self, val):
        if self.search(val) == False:
            for i in range(len(self.items)):
                if val < self.items[i]:
                    self.items.insert(i, val)
                    return
            self.items.append(val)

    def delete(self, val):
        for i in range(len(self.items)):
            if self.items[i] == val:
                self.items[i:i+1] = []
                break

    def search(self, val):
        for item in self.items:
            if item == val:
                return True
        return False

    def clear(self):
        self.items = []

    def display(self):
        return self.items

    @staticmethod
    def union(set_a, set_b):
        result = set_a.items[:]
        for item in set_b.items:
            if not SetOperations.search_static(result, item):
                result.append(item)
        result.sort()
        return result

    @staticmethod
    def intersection(set_a, set_b):
        result = []
        for item in set_a.items:
            if SetOperations.search_static(set_b.items, item):
                result.append(item)
            return result


    @staticmethod
    def set_difference(set_a, set_b):
        result = [item for item in set_a.items if SetOperations.search_static(set_b.items, item) == False]
        return result

    @staticmethod
    def sym_difference(set_a, set_b):
        diff1 = SetOperations.set_difference(set_a, set_b)
        diff2 = SetOperations.set_difference(set_b, set_a)
        return SetOperations.union_static(diff1, diff2)

    @staticmethod
    def is_subset(sub, sup):
        for item in sub.items:
            if SetOperations.search_static(sup.items, item) == False:
                return False
        return True

    @staticmethod
    def search_static(set_items, val):
        for item in set_items:
            if item == val:
                return True
        return False

    @staticmethod
    def union_static(set_a, set_b):
        result = set_a[:]
        for item in set_b:
            if SetOperations.search_static(result, item) == False:
                result.append(item)
        result.sort()
        return result  