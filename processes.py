import time
import multiprocessing
import threading

def calculate_primes(n):
    """
    Calculate prime numbers up to n.
    """
    primes = []
    for num in range(2, n+1):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            primes.append(num)
    return primes

def run_single_process():
    """
    Run calculate_primes() using a single process.
    """
    start_time = time.time()
    calculate_primes(10000)
    calculate_primes(10000)
    calculate_primes(10000)
    calculate_primes(10000)
    calculate_primes(10000)
    calculate_primes(10000)
    calculate_primes(10000)
    calculate_primes(10000)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Single process execution time: {execution_time:.2f} seconds")

def run_multiprocessing():
    """
    Run calculate_primes() using multiprocessing.
    """
    with multiprocessing.Pool(processes=8) as pool:
        start_time = time.time()
        results = pool.map(calculate_primes, [10000] * 8)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Multiprocessing execution time: {execution_time:.2f} seconds")
        # Combine the results from the processes
        primes = []
        for result in results:
            primes.extend(result)
        print(f"Found {len(primes)} primes using multiprocessing.")

def run_multithreading():
    """
    Run calculate_primes() using multithreading.
    """
    start_time = time.time()
    threads = []
    for i in range(1):
        t = threading.Thread(target=calculate_primes, args=(10000,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Multithreading execution time: {execution_time:.2f} seconds")

if __name__ == '__main__':
    run_single_process()
    run_multiprocessing()
    run_multithreading()