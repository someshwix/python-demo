import time

def profiler(func):
    '''Print the runtime of a function'''
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__} in {run_time:.4f} seconds")  # f-string
        return value
    return wrapper_timer

@profiler
def algorithm(num_times):  # Removed incorrect indentation
    for _ in range(num_times):  # Fixed `_in` to `_ in`
        sum([i**2 for i in range(1000)])  # Fixed indentation issue

# Test code
algorithm(1)
algorithm(999)