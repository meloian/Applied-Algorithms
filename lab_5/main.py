from matrix import Matrix
from vector import Vector
from lup import lup_decompose, lup_solve

if __name__ == "__main__":
    A_elements = [
        [10, 7, 8, 7, 6, 9],
        [7, 5, 6, 5, 4, 8],
        [8, 6, 10, 9, 7, 10],
        [7, 5, 9, 10, 6, 9],
        [6, 4, 7, 6, 10, 8],
        [9, 8, 10, 9, 8, 10]
    ]

    b_elements = [1, 2, 3, 4, 5, 6]

    A = Matrix(A_elements)
    b = Vector(b_elements)

    print("\n=== Matrix A ===")
    for row in A.entries:
        print(row)

    print("\n=== Vector b ===")
    print(b.values)

    # perform LUP decomposition
    A_decomposed, pi = lup_decompose(A.clone())
    if A_decomposed is not None:
        print("\n==> LUP Decomposition Successful")
    else:
        print("\nError during matrix decomposition: Matrix is singular")
        exit(1)

    # solve the system
    solution = lup_solve(A_decomposed, pi, b)
    if solution is not None:
        print("\n=== Solution to the system Ax = b ===")
        print("x =", solution.values)
    else:
        print("\nError solving the system")
        exit(1)

    Ax = A * solution
    print("\n=== Verification of Ax ===")
    print("Ax =", Ax.values)
    print("\n=== Original vector b ===")
    print("b =", b.values)

    # calculate the error
    error = [Ax.values[i] - b.values[i] for i in range(A.size)]
    print("\n=== Error (Ax - b) ===")
    print("Error =", error) 