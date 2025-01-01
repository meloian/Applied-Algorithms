import random 

def generate_random_list(size, low=0, high=1000000):
    return [random.randint(low, high) for _ in range(size)]

def generate_sizes(start, end, factor):
    sizes = []
    current = start
    while current <= end:
        sizes.append(current)
        current *= factor
    return sizes