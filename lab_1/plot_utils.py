import matplotlib.pyplot as plt

# plotting results

def plot_results(sizes, search_in_times, search_not_in_times, diff_times):
    plt.figure(figsize=(10, 8))

    plt.subplot(2, 1, 1)
    plt.plot(sizes, search_in_times, label='Search (In Set)')
    plt.plot(sizes, search_not_in_times, label='Search (Not In Set)')
    plt.xlabel('Set Size')
    plt.ylabel('Time (sec)')
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(sizes, diff_times, label='Set Difference')
    plt.xlabel('Set Size')
    plt.ylabel('Time (sec)')
    plt.legend()

    plt.tight_layout()
    plt.show()  