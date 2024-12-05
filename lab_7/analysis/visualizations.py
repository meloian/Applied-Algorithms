import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot_time_vs_size(df):
    os.makedirs('results/comparison_plots/time_vs_size', exist_ok=True)
    for data_name in df['data_name'].unique():
        plt.figure(figsize=(12,8))
        subset = df[df['data_name'] == data_name]
        sns.lineplot(data=subset, x='size', y='execution_time', hue='algorithm', markers=True)
        plt.xlabel('Size of input data')
        plt.ylabel('Execution time (s)')
        plt.title(f'Execution time depending on the size of input data ({data_name})')
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.xscale('linear')
        plt.yscale('linear')
        plt.tight_layout()
        plt.savefig(f'results/comparison_plots/time_vs_size/{data_name}_time_vs_size.png')
        plt.close()

def plot_metric_vs_size(df, metric):
    os.makedirs(f'results/comparison_plots/{metric}_vs_size', exist_ok=True)
    for data_name in df['data_name'].unique():
        plt.figure(figsize=(12,8))
        subset = df[df['data_name'] == data_name]
        sns.lineplot(data=subset, x='size', y=metric, hue='algorithm', markers=True)
        plt.xlabel('Size of input data')
        plt.ylabel(metric.replace('_', ' ').title())
        plt.title(f'{metric.replace("_", " ").title()} depending on the size of input data ({data_name})')
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.xscale('linear')
        plt.yscale('linear')
        plt.tight_layout()
        plt.savefig(f'results/comparison_plots/{metric}_vs_size/{data_name}_{metric}_vs_size.png')
        plt.close()

def generate_all_plots(df):
    os.makedirs('results/comparison_plots', exist_ok=True)
    plot_time_vs_size(df)
    metrics = ['comparisons', 'swaps']
    for metric in metrics:
        plot_metric_vs_size(df, metric)