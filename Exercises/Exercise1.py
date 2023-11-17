from multiprocessing import Process

def sum(max):
    res = 0
    for i in range(1, max+1):
        res = res + i
    print(res)

p1 = Process(target=sum, args=(10,))
p2 = Process(target=sum, args=(15,))
p3 = Process(target=sum, args=(25,))
p4 = Process(target=sum, args=(100,))
p5 = Process(target=sum, args=(156,))

if __name__ == "__main__":
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p5.join()
    print("All processes have been executed.")