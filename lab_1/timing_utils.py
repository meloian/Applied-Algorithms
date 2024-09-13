import random
import time

# timing and random set generation

def measure_time(operation, data, extra=None):
    total = 0
    for _ in range(1000):
        start = time.time()
        if extra:
            operation(data, extra)
        else:
            operation(data)
        total += time.time() - start
    return total / 1000

def create_random_set(size, min_val, max_val):
    return [random.uniform(min_val, max_val) for _ in range(size)] 