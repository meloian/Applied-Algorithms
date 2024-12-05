import random

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def median_of_three(arr, i, j, k):
    trio = [(arr[i], i), (arr[j], j), (arr[k], k)]
    trio.sort(key=lambda x: x[0])
    return trio[1][1]

def median_of_random_three(arr, low, high):
    if high - low + 1 < 3:
        return low if low == high else (low + high) // 2
    idxs = random.sample(range(low, high + 1), 3)
    return median_of_three(arr, *idxs)