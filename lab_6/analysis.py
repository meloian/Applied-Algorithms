import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import itertools
from merge_sort_recursive import merge_sort_recursive
from performance_metrics import PerformanceMetrics

def analyze_results(results):
    df = pd.DataFrame(results)
    print(df.to_string(index=False))

    df.to_csv('analysis_results.csv', index=False)

    plot_metrics(df)

def plot_metrics(df):
    metrics = ['Time (s)', 'Comparisons', 'Copy Ops', 'Memory (bytes)']
    sns.set(style="whitegrid")

    for metric in metrics:
        plt.figure(figsize=(12, 6))
        sns.lineplot(
            x='Data Size',
            y=metric,
            hue='Algorithm',
            data=df,
            marker='o',
            errorbar= None 
        )
        plt.title(f'{metric} by Algorithm and Data Size')
        plt.xlabel('Data Size')
        plt.ylabel(metric)
        plt.legend(title='Algorithm', bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
        plt.tight_layout()
        plt.savefig(f'{metric.replace(" ", "_")}_by_Algorithm_and_Data_Size.png')
        plt.show()