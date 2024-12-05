import random
from sorting_algorithms.utils import swap, median_of_three, median_of_random_three

class QuickSortLomuto:
    def __init__(self, pivot_type='last'):
        self.pivot_type = pivot_type
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
        if low < high:
            self.max_recursion_depth = max(self.max_recursion_depth, depth)
            p = self._partition(arr, low, high)
            self._quicksort(arr, low, p - 1, depth + 1)
            self._quicksort(arr, p + 1, high, depth + 1)

    def _choose_pivot(self, arr, low, high):
        if self.pivot_type == 'last':
            return high
        elif self.pivot_type == 'random':
            return random.randint(low, high)
        elif self.pivot_type == 'median_of_three':
            mid = (low + high) // 2
            return median_of_three(arr, low, mid, high)
        elif self.pivot_type == 'median_of_random_three':
            return median_of_random_three(arr, low, high)
        return high

    def _partition(self, arr, low, high):
        pivot_index = self._choose_pivot(arr, low, high)
        swap(arr, pivot_index, high)
        self.swaps += 1

        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            self.comparisons += 1
            if arr[j] <= pivot:
                i += 1
                swap(arr, i, j)
                self.swaps += 1
        swap(arr, i + 1, high)
        self.swaps += 1
        return i + 1