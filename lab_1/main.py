import random
from set_operations import SetOperations
from timing_utils import measure_time, create_random_set
from plot_utils import plot_results

def demonstrate_set_operations():
    set_a = SetOperations()
    set_b = SetOperations()

    for item in create_random_set(3, -50.0, 50.0):
        set_a.insert(item)
    for item in create_random_set(3, -50.0, 50.0):
        set_b.insert(item)

    print("Set A:", set_a.display())
    print("Set B:", set_b.display())

    set_a.insert(25.5)
    print("\nSet A after inserting 25.5:", set_a.display())

    set_a.delete(25.5)
    print("\nSet A after deleting 25.5:", set_a.display())

    union_result = SetOperations.union(set_a, set_b)
    print("\nUnion of Set A and Set B:", union_result)

    intersection_result = SetOperations.intersection(set_a, set_b)
    print("\nIntersection of Set A and Set B:", intersection_result)

    difference_result = SetOperations.set_difference(set_a, set_b)
    print("\nSet Difference (A / B):", difference_result)

    sym_difference_result = SetOperations.sym_difference(set_a, set_b)
    print("\nSymmetric Difference between Set A and Set B:", sym_difference_result)

    subset_check = SetOperations.is_subset(set_a, set_b)
    print(f"\nIs Set A a subset of Set B?: {'Yes' if subset_check else 'No'}")

# main function to run experiments

def perform_experiments():
    sizes = [100, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000]
    min_val, max_val = -10000.0, 10000.0

    search_in_times, search_not_in_times, diff_times = [], [], []

    for size in sizes:
        set_a = SetOperations()
        set_b = SetOperations() 

        for item in create_random_set(size, min_val, max_val):
            set_a.insert(item)
        for item in create_random_set(size, min_val, max_val):
            set_b.insert(item)

        print(f"\nSet size: {size}")

        rand_in = random.choice(set_a.display())
        search_in_times.append(measure_time(set_a.search, rand_in))
        print(f"Search time (element in the set): {search_in_times[-1]:.10f} sec")

        rand_not_in = max_val + 10000.0
        search_not_in_times.append(measure_time(set_a.search, rand_not_in))
        print(f"Search time (element is not in the set): {search_not_in_times[-1]:.10f} sec")

        diff_times.append(measure_time(SetOperations.set_difference, set_a, set_b))
        print(f"Time of difference: {diff_times[-1]:.10f} sec")

    plot_results(sizes, search_in_times, search_not_in_times, diff_times)

# demonstrate_set_operations() 
perform_experiments()