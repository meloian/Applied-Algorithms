def heapify(arr, n, i):
    # maintain sub-heap with root i
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapsort(arr):
    # heap sort in-place
    n = len(arr)
    # build heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    # extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0) 