from data_generator import *
from merge_sort_recursive import merge_sort_recursive
from merge_sort_iterative import merge_sort_iterative
from merge_sort_optimized import merge_sort_optimized
from merge_sort_variant import merge_sort_linked_list, array_to_linked_list, linked_list_to_array
from performance_metrics import PerformanceMetrics
import analysis

def main():
    import time
    import tracemalloc

    data_sizes = [1000, 5000, 10000, 15000]
    data_types = ['random', 'sorted', 'reverse', 'nearly_sorted', 'few_unique']
    sorting_algorithms = {
        'Recursive Merge Sort': merge_sort_recursive,
        'Iterative Merge Sort': merge_sort_iterative,
        'Optimized Merge Sort': lambda arr, metrics: merge_sort_optimized(arr, metrics, cutoff=32),
        'Linked List Merge Sort': merge_sort_linked_list
    }

    results = []

    for size in data_sizes:
        for data_type in data_types:
            if data_type == 'random':
                data = generate_random_data(size)
            elif data_type == 'sorted':
                data = generate_sorted_data(size)
            elif data_type == 'reverse':
                data = generate_reverse_sorted_data(size)
            elif data_type == 'nearly_sorted':
                data = generate_nearly_sorted_data(size)
            elif data_type == 'few_unique':
                data = generate_few_unique_data(size)
            else:
                continue

            for algo_name, algo_func in sorting_algorithms.items():
                metrics = PerformanceMetrics(store_sequence=False)
                tracemalloc.start()
                start_time = time.perf_counter()

                if algo_name == 'Linked List Merge Sort':
                    head = array_to_linked_list(data)
                    sorted_head, metrics = algo_func(head, metrics)
                    sorted_data = linked_list_to_array(sorted_head)
                else:
                    data_copy = data.copy()
                    sorted_data, metrics = algo_func(data_copy, metrics)

                metrics.time_elapsed = time.perf_counter() - start_time
                current, peak = tracemalloc.get_traced_memory()
                metrics.memory_usage = peak
                tracemalloc.stop()

                if sorted(sorted_data) != sorted_data:
                    print(f"Sort failed for {algo_name} with {data_type} data size {size}")
                else:
                    result = {
                        'Algorithm': algo_name,
                        'Data Type': data_type,
                        'Data Size': size,
                        'Time (s)': round(metrics.time_elapsed, 6),
                        'Comparisons': metrics.comparisons,
                        'Copy Ops': metrics.copy_operations,
                        'Memory (bytes)': metrics.memory_usage
                    }
                    results.append(result)

    analysis.analyze_results(results)

if __name__ == "__main__":
    main()