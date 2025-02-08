import threading
"""
This module demonstrates the use of threading in Python to perform
concurrent execution of two functions: calc_square and calc_cube.
Functions:
    calc_square(num): Calculates and prints the square of each number in the list `num`.
    calc_cube(num): Calculates and prints the cube of each number in the list `num`.
Execution:
    The main thread creates two threads to execute calc_square and calc_cube concurrently.
    It measures and prints the time taken for both threads to complete execution.
"""
import time

data = [4, 4, 6, 7, 2]

def calc_square(num):
    print("Calculate square of numbers")
    for n in num:
        time.sleep(0.3)
        print("Square of", n, "is", n * n)

def calc_cube(num):
    print("Calculate cube of numbers")
    for n in num:
        time.sleep(0.3)
        print("Cube of", n, "is", n * n * n)

if __name__ == "__main__":
    print("Main thread started")
    
    start = time.time()

    # Creating threads
    t1 = threading.Thread(target=calc_square, args=(data,))
    t2 = threading.Thread(target=calc_cube, args=(data,))

    # Starting threads
    t1.start()
    t2.start()

    # Wait for both threads to finish
    t1.join()
    t2.join()

    end = time.time()
    
    print("Main thread ended")
    print("Time taken with threading:", end - start)