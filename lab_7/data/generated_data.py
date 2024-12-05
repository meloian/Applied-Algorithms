import random

def generate_identical_elements(size, value=0):
    return [value] * size

def generate_sorted_data(size):
    return list(range(size))

def generate_random_data(size, low=0, high=1000000):
    return [random.randint(low, high) for _ in range(size)]

def generate_almost_sorted_data(size, swap_count=10):
    data = list(range(size))
    for _ in range(swap_count):
        idx1 = random.randint(0, size - 1)
        idx2 = random.randint(0, size - 1)
        data[idx1], data[idx2] = data[idx2], data[idx1]
    return data

def generate_reverse_sorted_data(size):
    return list(range(size, 0, -1))

def generate_triangular_data(size):
    half = size // 2
    first_half = list(range(half))
    middle = [half] if size % 2 == 1 else []
    second_half = first_half[::-1]
    return first_half + middle + second_half

def generate_few_unique_data(size, unique_count=5):
    return [random.randint(0, unique_count - 1) for _ in range(size)]