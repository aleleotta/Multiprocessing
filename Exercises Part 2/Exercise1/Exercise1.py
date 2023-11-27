from multiprocessing import *
import time

filePath = "Multiprocessing\\Exercises Part 2\\Exercise1\\vocals.txt"

def readVocals(vocalSelect):
    file = open(filePath, "r")
    vocals = file.read().lower()
    file.close()
    for vocal in vocals:
        count = 0
        if vocal == vocalSelect:
            count = count + 1
    print(count)

if __name__ == "__main__":
    print("Counting...\n\n")
    vocals = ["a", "e", "i", "o", "u"]
    for vocal in vocals:
        process = Process(target=readVocals, args=vocal)
        process.start()
    process.join()
    print(time.time())