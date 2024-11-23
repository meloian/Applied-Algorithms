# Iterative MergeSort with optimizations:
# =======================================
# - Cutoff to Insertion Sort: Sort small subarrays with Insertion Sort.
# - Stop-if-already-sorted: Skip merging if parts are already sorted.
# - Eliminate-the-copy-to-the-auxiliary-array: Minimize unnecessary copying.
# --------------------------------------------------------------------------
# Tracks time, comparisons, copies, and memory as required by the task.

from performance_metrics import PerformanceMetrics

# insertion sort for optimization
def insertion_sort(arr, left, right, metrics):
    for i in range(left + 1, right):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:  # shift elements until in place
            metrics.comparisons += 1
            arr[j + 1] = arr[j]
            metrics.copy_operations += 1
            j -= 1
        arr[j + 1] = key  # insert in the correct position
        metrics.copy_operations += 1

def merge_sort_optimized(arr, metrics=None, cutoff=15):
    
    if metrics is None:
        metrics = PerformanceMetrics()

    n = len(arr)
    temp_arr = arr.copy()
    metrics.copy_operations += n

    # cutoff to insertion sort
    for i in range(0, n, cutoff):
        insertion_sort(arr, i, min(i + cutoff, n), metrics)

    width = cutoff
    while width < n:
        for i in range(0, n, 2 * width):
            left = i
            mid = min(i + width, n)
            right = min(i + 2 * width, n)

            # stop-if-already-sorted
            if mid < n and arr[mid - 1] <= arr[mid]:
                metrics.comparisons += 1
                continue

            # merge two halves with slices
            l, r = left, mid
            k = left
            while l < mid and r < right:
                metrics.comparisons += 1
                if arr[l] <= arr[r]:
                    temp_arr[k] = arr[l]
                    l += 1
                else:
                    temp_arr[k] = arr[r]
                    r += 1
                k += 1

            while l < mid:
                temp_arr[k] = arr[l]
                metrics.copy_operations += 1
                l += 1
                k += 1

            while r < right:
                temp_arr[k] = arr[r]
                metrics.copy_operations += 1
                r += 1
                k += 1

            # efficient copying back to the array
            arr[left:right] = temp_arr[left:right]
            metrics.copy_operations += (right - left)

        width *= 2

    return arr, metrics