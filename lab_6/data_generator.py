import random

def generate_random_data(size):
    return [random.randint(0, size) for _ in range(size)]

def generate_sorted_data(size):
    return list(range(size))

def generate_reverse_sorted_data(size):
    return list(range(size, 0, -1))

def generate_nearly_sorted_data(size, swaps=10):
    data = list(range(size))
    for _ in range(swaps):
        i = random.randint(0, size - 1)
        j = random.randint(0, size - 1)
        data[i], data[j] = data[j], data[i]
    return data

def generate_few_unique_data(size, unique_values=5):
    values = [random.randint(0, size) for _ in range(unique_values)]
    return [random.choice(values) for _ in range(size)] 