# This is the iterative (Bottom-Up) MergeSort.
# ============================================
# - Starts with subarrays of size 1.
# - Merges them into sorted subarrays.
# - Doubles the subarray size each pass.
# - Repeats until the whole array is sorted.
# --------------------------------------------------------------------
# Tracks time, comparisons, copies, and memory as required by the task.

from performance_metrics import PerformanceMetrics

def merge_sort_iterative(arr, metrics=None):

    if metrics is None:
        metrics = PerformanceMetrics()

    width = 1  # size 1 subarrays
    n = len(arr)
    temp_arr = arr.copy()  # for merging
    metrics.copy_operations += n

    while width < n:
        for i in range(0, n, 2 * width):  # merge subarrays
            left = i
            mid = min(i + width, n)
            right = min(i + 2 * width, n)

            l, r = left, mid
            for k in range(left, right):  # merge into temp_arr
                if l < mid and (r >= right or arr[l] <= arr[r]):
                    temp_arr[k] = arr[l]
                    metrics.comparisons += 1
                    metrics.copy_operations += 1
                    l += 1
                else:
                    temp_arr[k] = arr[r]
                    metrics.comparisons += 1
                    metrics.copy_operations += 1
                    r += 1

        arr, temp_arr = temp_arr, arr  # swap arrays
        width *= 2  # double the size

    return arr, metrics