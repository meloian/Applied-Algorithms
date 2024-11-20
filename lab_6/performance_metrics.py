import tracemalloc

class PerformanceMetrics:
    def __init__(self, store_sequence=False):
        self.comparisons = 0
        self.copy_operations = 0
        self.time_elapsed = 0.0
        self.memory_usage = 0
        # flag to track comparison details
        self.store_sequence = store_sequence
        if self.store_sequence:
            self.comparison_sequence = []
        else:
            self.comparison_sequence = None

    def reset(self):
        self.comparisons = 0
        self.copy_operations = 0
        self.time_elapsed = 0.0
        self.memory_usage = 0
        # reset if tracking
        if self.store_sequence:
            self.comparison_sequence = []
        else:
            self.comparison_sequence = None 

    def measure_memory(self):
        current, peak = tracemalloc.get_traced_memory()
        self.memory_usage = peak