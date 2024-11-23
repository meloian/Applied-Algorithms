# This is the recursive (Top-Down) MergeSort. 
# ===========================================
# - Splits the array into two halves recursively.
# - Sorts each half independently.
# - Merges the sorted halves back into one array.
# ------------------------------------------------------------
# Tracks time, comparisons, copies, and memory as the task requires.

from performance_metrics import PerformanceMetrics

def merge_sort_recursive(arr, metrics=None):

    if metrics is None:
        metrics = PerformanceMetrics()

    # split and merge recursively
    def merge_sort(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            L = arr[:mid]  # left half
            R = arr[mid:]  # right half

            metrics.copy_operations += len(L) + len(R)

            merge_sort(L)
            merge_sort(R)

            # merge the halves
            i = j = k = 0
            
            while i < len(L) and j < len(R):
                metrics.comparisons += 1  # сount comparisons
                if metrics.store_sequence and metrics.comparison_sequence is not None:
                    metrics.comparison_sequence.append((L[i], R[j]))  # track comparison details 
                    
                if L[i] <= R[j]:
                    arr[k] = L[i]
                    metrics.copy_operations += 1
                    i += 1
                else:
                    arr[k] = R[j]
                    metrics.copy_operations += 1
                    j += 1
                k += 1

            # copy remaining elements
            while i < len(L):
                arr[k] = L[i]
                metrics.copy_operations += 1
                i += 1
                k += 1
            while j < len(R):
                arr[k] = R[j]
                metrics.copy_operations += 1
                j += 1
                k += 1

    merge_sort(arr)

    return arr, metrics