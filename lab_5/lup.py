from vector import Vector

def lup_decompose(A):
    n = A.size
    pi = list(range(n))
    for k in range(n):
        # find k' = argmax_{i=k to n-1} |A[i][k]|
        max_val = 0
        k_prime = -1
        for i in range(k, n):
            if abs(A[i][k]) > max_val:
                max_val = abs(A[i][k])
                k_prime = i
        if A[k_prime][k] == 0:
            raise ValueError("Matrix is singular")
        # swap rows k and k' in A
        A.interchange_rows(k, k_prime)
        # swap π[k] and π[k']
        pi[k], pi[k_prime] = pi[k_prime], pi[k]
        for i in range(k + 1, n):
            A[i][k] = A[i][k] / A[k][k]
            for j in range(k + 1, n):
                A[i][j] -= A[i][k] * A[k][j]
    return A, pi

def lup_solve(A, pi, b):
    n = A.size
    x = [0] * n
    y = [0] * n
    # replacement for Ly = Pb
    for i in range(n):
        total = b[pi[i]]
        for j in range(i):
            total -= A[i][j] * y[j]
        y[i] = total
    # inverse replacement for Ux = y
    for i in reversed(range(n)):
        total = y[i]
        for j in range(i + 1, n):
            total -= A[i][j] * x[j]
        x[i] = total / A[i][i]
    return Vector(x)