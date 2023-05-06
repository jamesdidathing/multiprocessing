from multiprocessing import Process
import time
import random
from functools import reduce
start = time.time()

def multiply(count):
    list_random = random.sample(range(1000000), count)
    return reduce(lambda x, y: x*y, list_random)

count = 80000
process1 = Process(target=multiply, args=(count,))
process2 = Process(target=multiply, args=(count,))
process3 = Process(target=multiply, args=(count,))
process4 = Process(target=multiply, args=(count,))

if __name__ == 'main':

    process1.start()
    process2.start()
    process3.start()
    process4.start()

    process1.join()
    process2.join()
    process3.join()
    process4.join()


end = time.time()
total_time = end - start
print(f"Execution time: {total_time}")