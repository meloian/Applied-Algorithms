import random
import time
import matplotlib.pyplot as plt
import os

from heapsort import heapsort
from priority_queue import PriorityQueue
from data import generate_random_list , generate_sizes

def demo_priority_queue():
    pq = PriorityQueue()
    operations_count = 10000
    push_times = []
    pop_times = []

    print("priority queue demo")
    print("===================")

    # measure push
    for _ in range(operations_count):
        start_push = time.time()
        pq.push(random.randint(0, 100000))
        end_push = time.time()
        push_times.append(end_push - start_push)

    # measure pop
    for _ in range(operations_count):
        start_pop = time.time()
        pq.pop()
        end_pop = time.time()
        pop_times.append(end_pop - start_pop)

    avg_push_time = sum(push_times) / len(push_times)
    avg_pop_time = sum(pop_times) / len(pop_times)
    print(f"average push time: {avg_push_time:.6e} s")
    print(f"average pop time:  {avg_pop_time:.6e} s\n")

def demo_heapsort():
    print("heap sort demo")
    print("==============")

    os.makedirs("result", exist_ok=True)

    sizes = generate_sizes(start=1000, end = 5000000, factor = 2)
    data_types = {
        "random": lambda s: generate_random_list(s),
        "sorted": lambda s: list(range(s)),
        "reversed": lambda s: list(range(s, 0, -1)),
    }

    # store results for plotting
    results = {dtype: [] for dtype in data_types}

    # run tests
    for dtype, generator in data_types.items():
        print(f"data type: {dtype}")
        for s in sizes:
            arr = generator(s)
            start_time = time.time()
            heapsort(arr)
            end_time = time.time()
            elapsed = end_time - start_time
            results[dtype].append((s, elapsed))
            print(f"  size: {s}, time: {elapsed:.6f} s")
        print("")

    # plot results
    plt.figure(figsize=(8, 5))
    for dtype, data in results.items():
        x_vals = [item[0] for item in data]
        y_vals = [item[1] for item in data]
        plt.plot(x_vals, y_vals, marker='o', label=dtype)

    plt.title("heap sort time vs. size")
    plt.xlabel("size")
    plt.ylabel("time (s)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    # save plot to result folder
    plt.savefig("result/heap_sort_time_vs_size.png")
    plt.show()

def main():
    # priority queue
    demo_priority_queue()

    # heap sort
    demo_heapsort()

if __name__ == "__main__":
    main()