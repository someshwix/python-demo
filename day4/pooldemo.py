import multiprocessing as mp
import os

def square(n):
    print("Worker process with PID: {0}, computing square of {1}".format(os.getpid(), n))
    return n * n  # Returning instead of incorrectly calling `result(n * n)`

if __name__ == '__main__':
    num_cores = mp.cpu_count()
    print("This kernel has", num_cores, "cores")

    mylist = [1, 1000, 36348, 4, 5]

    with mp.Pool(processes=num_cores) as p:  # Explicitly setting process count
        result = p.map(square, mylist)  # Correct function call

    print("Squared values:", result)  # Printing results outside the pool