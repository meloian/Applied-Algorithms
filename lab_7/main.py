import os
import sys
from data.generated_data import (
    generate_identical_elements,
    generate_sorted_data,
    generate_random_data,
    generate_almost_sorted_data,
    generate_reverse_sorted_data,
    generate_triangular_data,
    generate_few_unique_data
)
from analysis.comparison import run_comparisons
from analysis.visualizations import generate_all_plots
import pandas as pd

def main():

    recursion_limit = 100000
    sys.setrecursionlimit(recursion_limit)
    os.makedirs('results/comparison_plots', exist_ok=True)

    sizes = [1000, 5000, 10000, 20000, 50000]

    data_generators = {
        'identical_elements': generate_identical_elements,
        'sorted_data': generate_sorted_data,
        'random_data': generate_random_data,
        'almost_sorted_data': generate_almost_sorted_data,
        'reverse_sorted_data': generate_reverse_sorted_data,
        'triangular_data': generate_triangular_data,
        'few_unique_data': generate_few_unique_data
    }

    try:
        df = run_comparisons(data_generators, sizes)
    except Exception as e:
        print(f"Error while making comparisons: {e}")
        return

    generate_all_plots(df)

if __name__ == '__main__':
    main()