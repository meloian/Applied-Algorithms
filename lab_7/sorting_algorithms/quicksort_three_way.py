import random
from sorting_algorithms.utils import swap, median_of_random_three

class QuickSortThreeWay:
    def __init__(self):
        self.pivot_type = 'median_of_random_three'
        self.comparisons = 0
        self.swaps = 0
        self.max_recursion_depth = 0

    def sort(self, arr):
        self.comparisons = 0
        self.swaps = 0
        self.max_recursion_depth = 0
        self._quicksort(arr, 0, len(arr) - 1, 0)
        return arr

    def _quicksort(self, arr, low, high, depth):
        # base condition for recursion
        if low < high:
            self.max_recursion_depth = max(self.max_recursion_depth, depth)
            # partition the array into three
            lt, gt = self._partition(arr, low, high)
            # recursively sort elements less than the pivot
            self._quicksort(arr, low, lt - 1, depth + 1)
            # recursively sort elements greater than the pivot
            self._quicksort(arr, gt + 1, high, depth + 1)

    def _partition(self, arr, low, high):
        # choose pivot using median of three random elements
        pivot_index = median_of_random_three(arr, low, high)
        pivot = arr[pivot_index]
        # move pivot to start of array
        swap(arr, pivot_index, low)
        self.swaps += 1
        
        # pointers for partitioning
        lt = low       # arr[low..lt-1] < pivot
        i = low + 1    # arr[lt..i-1] == pivot
        gt = high      # arr[gt+1..high] > pivot

        while i <= gt:
            self.comparisons += 1
            if arr[i] < pivot:
                # element in first partition
                swap(arr, lt, i)
                self.swaps += 1
                lt += 1
                i += 1
            elif arr[i] > pivot:
                # element in third partition
                swap(arr, i, gt)
                self.swaps += 1
                gt -= 1
            else:
                # element in second partition
                i += 1
        return lt, gt