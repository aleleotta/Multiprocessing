from multiprocessing import Process

def sum(min, max):
    res = 0
    if min > max:
        min, max = max, min
    for i in range(min, max+1):
        res = res + i
    print(res)

p1 = Process(target=sum, args=(1, 10))
p2 = Process(target=sum, args=(10, 55))
p3 = Process(target=sum, args=(100, 1000))
p4 = Process(target=sum, args=(13145, 55436))
p5 = Process(target=sum, args=(100000000, 55075))

if __name__ == "__main__":
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p5.join()
    print("All processes have been executed.")