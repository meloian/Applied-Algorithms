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
        # base condition for recursion
        if low < high:
            self.max_recursion_depth = max(self.max_recursion_depth, depth)
            # partition the array into three using two pivots
            lp, rp = self._partition(arr, low, high)
            # recursively sort the three parts
            self._dual_pivot_quicksort(arr, low, lp - 1, depth + 1)
            self._dual_pivot_quicksort(arr, lp + 1, rp - 1, depth + 1)
            self._dual_pivot_quicksort(arr, rp + 1, high, depth + 1)

    def _partition(self, arr, low, high):
        # ensure the pivot1 is smaller than pivot1
        self.comparisons += 1
        if arr[low] > arr[high]:
            swap(arr, low, high)
            self.swaps += 1

        # initialize 
        pivot1 = arr[low]
        pivot2 = arr[high]

        # pointers for partitioning
        i = low + 1
        lt = low + 1  # boundary for elements less than pivot1
        gt = high - 1 # boundary for elements greater than pivot2

        while i <= gt:
            self.comparisons += 1
            if arr[i] < pivot1:
                # put element in first partition
                swap(arr, i, lt)
                self.swaps += 1
                lt += 1
                i += 1
            elif arr[i] > pivot2:
                # put element in third partition
                swap(arr, i, gt)
                self.swaps += 1
                gt -= 1
            else:
                # element in second partition
                i += 1
        
        # place the pivots in correct positions
        lt -= 1
        gt += 1
        swap(arr, low, lt)
        self.swaps += 1
        swap(arr, high, gt)
        self.swaps += 1

        return lt, gt