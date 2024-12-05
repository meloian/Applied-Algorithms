import pandas as pd
from analysis.metrics import collect_metrics
from sorting_algorithms.quicksort_lomuto import QuickSortLomuto
from sorting_algorithms.quicksort_hoare import QuickSortHoare
from sorting_algorithms.quicksort_dual_pivot import QuickSortDualPivot
from sorting_algorithms.quicksort_three_way import QuickSortThreeWay

def run_comparisons(data_generators, sizes):
    results = []
    algorithms = get_algorithms()
    for size in sizes:
        for data_name, data_generator in data_generators.items():
            data = data_generator(size)
            for alg_name, algorithm in algorithms.items():
                print(f"Running {alg_name} on {data_name} of size {size}")
                metrics = collect_metrics(algorithm, data)
                results.append({'data_name': data_name, 'size': size, 'algorithm': alg_name, **metrics})
    df = pd.DataFrame(results)
    df.to_csv('results/performance_data.csv', index=False)
    return df

def get_algorithms():
    pivot_types = ['last', 'random', 'median_of_three', 'median_of_random_three']
    algorithms = {}
    for p in pivot_types:
        algorithms[f'QuickSortLomuto_{p}'] = QuickSortLomuto(p)
        algorithms[f'QuickSortHoare_{p}'] = QuickSortHoare(p)
    algorithms['QuickSortDualPivot'] = QuickSortDualPivot()
    algorithms['QuickSortThreeWay'] = QuickSortThreeWay()
    return algorithms 