from sorting_algorithms.utils import swap

class QuickSortDualPivot:
    def __init__(self):
        self.pivot_type = 'dual_pivot'
        self.comparisons = 0
        self.swaps = 0
        self.max_recursion_depth = 0

    def sort(self, arr):
        self.comparisons = 0
        self.swaps = 0
        self.max_recursion_depth = 0
        self._dual_pivot_quicksort(arr, 0, len(arr) - 1, 0)
        return arr

    def _dual_pivot_quicksort(self, arr, low, high, depth):
        if low < high:
            self.max_recursion_depth = max(self.max_recursion_depth, depth)
            lp, rp = self._partition(arr, low, high)
            self._dual_pivot_quicksort(arr, low, lp - 1, depth + 1)
            self._dual_pivot_quicksort(arr, lp + 1, rp - 1, depth + 1)
            self._dual_pivot_quicksort(arr, rp + 1, high, depth + 1)

    def _partition(self, arr, low, high):
        self.comparisons += 1
        if arr[low] > arr[high]:
            swap(arr, low, high)
            self.swaps += 1

        pivot1 = arr[low]
        pivot2 = arr[high]

        i = low + 1
        lt = low + 1
        gt = high - 1

        while i <= gt:
            self.comparisons += 1
            if arr[i] < pivot1:
                swap(arr, i, lt)
                self.swaps += 1
                lt += 1
                i += 1
            elif arr[i] > pivot2:
                swap(arr, i, gt)
                self.swaps += 1
                gt -= 1
            else:
                i += 1
        lt -= 1
        gt += 1
        swap(arr, low, lt)
        self.swaps += 1
        swap(arr, high, gt)
        self.swaps += 1

        return lt, gt