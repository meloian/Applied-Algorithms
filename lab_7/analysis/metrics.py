import time
import psutil
import os
import threading

def monitor_memory(process, interval, stop_event, memory_usage_list):
    while not stop_event.is_set():
        mem = process.memory_info().rss # get current memory usage (bytes)
        memory_usage_list.append(mem)
        time.sleep(interval)

def collect_metrics(algorithm, data):

    process = psutil.Process(os.getpid()) # get current process
    
    data_copy = data.copy()

    memory_usage_list = []
    stop_event = threading.Event() # event to end monitoring

    # start thread to monitor memory usage
    monitor_thread = threading.Thread(target=monitor_memory, args=(process, 0.001, stop_event, memory_usage_list))
    monitor_thread.start()

    error_message = None
    is_correct = False

    try:
        start_time = time.perf_counter()
        algorithm.sort(data_copy)
        end_time = time.perf_counter()
        
        is_correct = data_copy == sorted(data_copy)
    except RecursionError:
        # handle recursion depth error.
        stop_event.set()
        monitor_thread.join()
        is_correct = False
        error_message = 'RecursionError'
        return {
            'execution_time': None,
            'memory_usage': None,
            'comparisons': algorithm.comparisons,
            'swaps': algorithm.swaps,
            'recursion_depth': algorithm.max_recursion_depth,
            'correctness': is_correct,
            'error': error_message
        }
    except Exception as e:
        stop_event.set()
        monitor_thread.join()
        is_correct = False
        error_message = str(e)
        return {
            'execution_time': None,
            'memory_usage': None,
            'comparisons': algorithm.comparisons,
            'swaps': algorithm.swaps,
            'recursion_depth': algorithm.max_recursion_depth,
            'correctness': is_correct,
            'error': error_message
        }

    stop_event.set()
    monitor_thread.join()

    if memory_usage_list:
        peak_memory = max(memory_usage_list)
        mem_before = memory_usage_list[0]
        memory_usage = (peak_memory - mem_before) / (1024 * 1024)
    else:
        mem_before = process.memory_info().rss
        peak_memory = mem_before
        memory_usage = 0.0

    execution_time = end_time - start_time
    comparisons = algorithm.comparisons
    swaps = algorithm.swaps
    recursion_depth = getattr(algorithm, 'max_recursion_depth', None)

    return {
        'execution_time': execution_time,
        'memory_usage': memory_usage,
        'comparisons': comparisons,
        'swaps': swaps,
        'recursion_depth': recursion_depth,
        'correctness': is_correct,
        'error': error_message
    } 