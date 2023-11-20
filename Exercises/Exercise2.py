from multiprocessing import *
import time

def sum(max):
    res = 0
    for i in range(1, max+1):
        res = res + i
    print(res)

if __name__ == "__main__":
    with Pool(processes=3) as pool:
        numbers = [10, 15, 25, 100, 156]
        result = pool.map(sum, numbers)
    print(str(result) + "\n")