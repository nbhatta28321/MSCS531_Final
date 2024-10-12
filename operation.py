import time
import multiprocessing 

# some operation
def operation(n):
    # assuming this is time consuming
    time.sleep(1)
    return n * n

# Using single main thread
# this function simply loop to the range up to 4 and give the square root.
def normal():
    start_time = time.time()
    arr = []
    for i in range(5):
        arr.append(operation(i))
    end_time = time.time()
    print(f"Single thread time: {end_time - start_time:.2f} seconds: {arr}")
    return

# Using multiple threads
# this function creates a number of processes to be created for parallely operating square root
def parallel():
    start_time = time.time()
    pool = multiprocessing.Pool(processes=4)
    arr = pool.map(operation, range(5))
    end_time = time.time()
    print(f"Parallel execution time: {end_time - start_time:.2f} seconds: {arr}")
    return

if __name__ == '__main__':
    normal()
    parallel()
