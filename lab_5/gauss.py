def find_invertible(A, i, j):
    n = A.size
    k = i
    while k < n:
        if A[k][j] != 0:
            return k
        k += 1
    return n  # if no invertible element is found

def gauss_elimination(A):
    n = A.size
    swapnum = 0
    j = 0
    i = 0
    while i < n and j < n:
        if A[i][j] == 0:
            k = find_invertible(A, i, j)
            if k < n:
                A.interchange_rows(i, k)
                swapnum += 1
                # det(A) = (-1) ** swapnum * (A[0][0] * A[1][1] * ... * A[n-1][n-1])
            else:
                j += 1
                if j > n:
                    return A, swapnum
                continue
        for t in range(i + 1, n):
            factor = A[t][j] / A[i][j]
            for s in range(j, n):
                A[t][s] -= factor * A[i][s]
        i += 1
        j += 1
    return A, swapnum