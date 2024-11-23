# This script finds the minimum and maximum number of comparisons for MergeSort.
# ================================================================================
# It checks all possible permutations for arrays of a given size.
# -----------------------------------------------------------------
# For each size, it identifies:
# - The permutation with the fewest comparisons.
# - The permutation with the most comparisons.

import itertools
import pandas as pd
from merge_sort_recursive import merge_sort_recursive
from performance_metrics import PerformanceMetrics

def compute_min_max_comparisons(max_size=8):
    results = []

    for size in range(1, max_size + 1):
        print(f'\nCalculating the minimum and maximum number of comparisons for array size {size}...')
        all_permutations = list(itertools.permutations(range(size), size))  # generate all permutations of the given size
        min_comparisons = None
        max_comparisons = None
        min_perm = None
        max_perm = None
        min_sequence = []
        max_sequence = []

        total_perms = len(all_permutations)
        for idx, perm in enumerate(all_permutations):

            data = list(perm)
            metrics = PerformanceMetrics(store_sequence=True)
            sorted_data, metrics = merge_sort_recursive(data, metrics)

            comparisons = metrics.comparisons

            # update minimum comparison data
            if min_comparisons is None or comparisons < min_comparisons:
                min_comparisons = comparisons
                min_perm = perm
                min_sequence = metrics.comparison_sequence.copy()

            # update maximum comparison data
            if max_comparisons is None or comparisons > max_comparisons:
                max_comparisons = comparisons
                max_perm = perm
                max_sequence = metrics.comparison_sequence.copy()

            metrics.comparison_sequence.clear()

            if total_perms > 100 and idx % (total_perms // 10 + 1) == 0:
                print(f'Progress: {idx}/{total_perms} permutations processed.')

        result = {
            'Size': size,
            'Min Comparisons': min_comparisons,
            'Min Permutation': min_perm,
            'Min Sequence': min_sequence,
            'Max Comparisons': max_comparisons,
            'Max Permutation': max_perm,
            'Max Sequence': max_sequence
        }
        results.append(result)

    print("\nExact minimum and maximum number of comparisons for each array size:")

    for res in results:
        print(f"\nArray size: {res['Size']}")
        print(f"Minimum number of comparisons: {res['Min Comparisons']} to permute {res['Min Permutation']}")
        print(f"Sequence of comparisons: {res['Min Sequence']}")
        print(f"Maximum number of comparisons: {res['Max Comparisons']} to permute {res['Max Permutation']}")
        print(f"Sequence of comparisons: {res['Max Sequence']}")

    min_max_df = pd.DataFrame(results)
    min_max_df.to_csv('min_max_comparisons.csv', index=False)
    print("\nResults saved to file 'min_max_comparisons.csv'.")

    plot_min_max_comparisons(min_max_df)

def plot_min_max_comparisons(df):
    import matplotlib.pyplot as plt

    plt.figure(figsize=(10, 6))
    plt.plot(df['Size'], df['Min Comparisons'], label='Minimal comparisons', marker='o')
    plt.plot(df['Size'], df['Max Comparisons'], label='Maximal comparisons', marker='x')
    plt.title('Minimum and maximum number of comparisons by array size')
    plt.xlabel('Array size')
    plt.ylabel('Number of comparisons')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('min_max_comparisons_plot.png')
    plt.show()
    print("The graph is saved as 'min_max_comparisons_plot.png'.")

if __name__ == "__main__":
    compute_min_max_comparisons(max_size=11) 