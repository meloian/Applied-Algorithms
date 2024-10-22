class Vector:
    def __init__(self, elements):
        self.values = elements  # elements should be a list of numbers

    def __add__(self, other):
        new_values = []
        for x, y in zip(self.values, other.values):
            new_values.append(x + y)
        return Vector(new_values)

    def __sub__(self, other):
        # subtract
        new_values = []
        for x, y in zip(self.values, other.values):
            new_values.append(x - y)
        return Vector(new_values)

    def __mul__(self, scalar):
        # multiply
        new_values = []
        for x in self.values:
            new_values.append(scalar * x)
        return Vector(new_values)

    def __rmul__(self, scalar):
        # allow scalar multiplication from left
        return self.__mul__(scalar)

    def dimension(self):
        # length of the vector
        return len(self.values)

    def __getitem__(self, index):
        # item by index
        return self.values[index]

    def __str__(self):
        # string representation
        return str(self.values)