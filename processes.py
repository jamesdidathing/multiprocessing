from multiprocessing import Process
from multiprocessing import Pool
import random
from functools import reduce
import time

def pool_square(a):
    print("Process begins here:")
    square = a*a
    time.sleep(1)
    print("Process end.")

def norm_square(a):
    square = a*a
    time.sleep(1)
    
def pool():
    pool_start_t = time.time()
    pool = Pool() # number of cores that the pool will use. when one core is free, the next process will use it
    pool.map(pool_square, range(0,9))
    pool.close
    pool_end_t = time.time()
    return pool_end_t - pool_start_t

def norm():
    norm_start_t = time.time()
    for i in range(0,9):
        norm_square(i)
    norm_end_t = time.time()
    return norm_end_t - norm_start_t

if __name__ == '__main__':

    print(f"Time taken with Pool is {pool()}")
    print(f"Time taken without Pool is {norm()}")