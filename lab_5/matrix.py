from vector import Vector

class Matrix:
    def __init__(self, elements):
        self.entries = elements  # elements should be a list of row lists
        self.size = len(elements)
        if any(len(row) != self.size for row in elements):
            raise ValueError("Matrix must be square")

    def __add__(self, other):
        result = []
        for row_self, row_other in zip(self.entries, other.entries):
            new_row = []
            for x, y in zip(row_self, row_other):
                new_row.append(x + y)
            result.append(new_row)
        return Matrix(result)

    def __sub__(self, other):
        # subtract
        result = []
        for row_self, row_other in zip(self.entries, other.entries):
            new_row = []
            for x, y in zip(row_self, row_other):
                new_row.append(x - y)
            result.append(new_row)
        return Matrix(result)

    def __mul__(self, other):
        if isinstance(other, Matrix):
            # multiplication
            result = [[0 for _ in range(self.size)] for _ in range(self.size)]
            for i in range(self.size):
                for j in range(self.size):
                    for k in range(self.size):
                        result[i][j] += self.entries[i][k] * other.entries[k][j]
            return Matrix(result)
        elif isinstance(other, Vector):
            # matrix-vector multiplication
            new_values = []
            for i in range(self.size):
                total = 0
                for j in range(self.size):
                    total += self.entries[i][j] * other[j]
                new_values.append(total)
            return Vector(new_values)
        else:
            raise ValueError("Unsupported multiplication")

    def __getitem__(self, index):
        # row by index
        return self.entries[index]

    def __str__(self):
        # string representation
        rows_as_strings = []
        for row in self.entries:
            rows_as_strings.append(' '.join(map(str, row)))
        return '\n'.join(rows_as_strings)

    def clone(self):
        # create a copy
        new_entries = []
        for row in self.entries:
            new_entries.append(row[:])
        return Matrix(new_entries)

    def interchange_rows(self, i, j):
        # swap rows i and j
        self.entries[i], self.entries[j] = self.entries[j], self.entries[i] 