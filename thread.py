import threading
import random
import time
import multiprocessing
from functools import reduce

def square(a):
    print("Process begins here:")
    square = a*a
    time.sleep(1)
    print("Process end.")

def main():
    threads = []
    for n in range(1,9):
        t = threading.Thread(target=square, args=(n,))
        threads.append(t)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


             
if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Time: {end-start}")
