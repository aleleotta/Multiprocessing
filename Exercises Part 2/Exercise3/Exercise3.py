from multiprocessing import *
from random import uniform

def generateRandoms(connection, filePath, studentName):
    collection = []
    for i in range(6):
        num = uniform(0, 10)
        collection.append(num)
    writer = open(filePath, "w")
    for num in collection:
        writer.write(str(num) + "\n")
    pack = (filePath, studentName)
    connection.send(pack)
    writer.close()

def calcAverage(connection, connection1):
    pack = connection.recv()
    filePath, studentName = pack
    doc = open(filePath, "r")
    numCollection = doc.readlines()
    doc.close()
    sum = 0
    count = 0
    for num in numCollection:
        sum = sum + round(float(num))
        count = count + 1
    average = sum / count
    filePath = "Exercises Part 2\\Exercise3\\averages.txt"
    doc = open(filePath, "a")
    doc.write(str(average) + " " + studentName + "\n")
    doc.close()
    connection1.send(filePath)

def findMax(connection):
    filePath = connection.recv()
    doc = open(filePath, "r")
    lines = doc.readlines()
    doc.close()
    averages = []
    for line in lines:
        number = ""
        for char in line:
            if char.isdigit() or char == ".":
                number = number + char
        averages.append(number)
    maxGrade = 0.0
    for average in averages:
        if float(average) > maxGrade:
            maxGrade = float(average)
    currentLine = ""
    for line in lines:
        currentLine = line
        number = ""
        for char in line:
            if not char.isdigit() and not char == ".":
                break
            number = number + str(char)
        if maxGrade < float(number):
            maxGrade = float(number)
    print("Max grade: " + currentLine)

if __name__ == "__main__":
    doc = open("Exercises Part 2\\Exercise3\\averages.txt", "w")
    doc.write("")
    doc.flush()
    doc.close()
    filePath = "Exercises Part 2\\Exercise3"
    studentName = "student"
    left, right = Pipe()
    left1, right1 = Pipe()
    for i in range(10):
        studentName = studentName + str(i+1)
        filePath = "Exercises Part 2\\Exercise3\\Students\\" + studentName + ".txt"
        p1 = Process(target=generateRandoms, args=(left, filePath, studentName,))
        p2 = Process(target=calcAverage, args=(right, left1,))
        p3 = Process(target=findMax, args=(right1,))
        p1.start()
        p2.start()
        p3.start()
        p1.join()
        p2.join()
        p3.join()
        studentName = "student"

"""
En este ejercicio debes implementar los siguientes procesos y el Main como se explica a continuación:

Proceso 1: Genera 6 números aleatorios entre 1 y 10, ambos inclusive, y los guarda en un fichero.
           Estos números deben contener decimales. La ruta a este fichero se le indicará como parámetro de entrada.
           Estos 6 números representan las notas de un alumno.

Proceso 2: Lee un fichero pasado por parámetro que contiene las notas de un alumno,
           cada una en una línea distinta, y realiza la media de las notas.
           También recibe como parámetro el nombre del alumno.
           Esta media se almacenará en un fichero de nombre medias.txt.
           Al lado de cada media debe aparecer el nombre del alumno, separados por un espacio.

Proceso 3: Lee el fichero medias.txt.
           En cada línea del fichero aparecerá una nota, un espacio y el nombre del alumno.
           Este proceso debe leer el fichero y obtener la nota máxima.
           Imprimirá por pantalla la nota máxima junto con el nombre del alumno que la ha obtenido.
           
Main: Lanza 10 veces el primer proceso de forma concurrente.
      Cada una de esas veces debe guardarse el resultado en un fichero distinto.
      Es decir, al final tiene que haber 10 ficheros distintos con las notas de cada alumno.
      Pon a los ficheros nombres como Alumno1.txt, Alumno2.txt, …, Alumno10.txt.

A continuación, se debe lanzar el proceso 2 que toma los ficheros creados en el paso anterior como entrada.
Por lo que el proceso 2 se lanzará 10 veces también,
una por cada fichero generado por el proceso 1,
y realizarlo todo de forma simultánea/concurrente.
Es decir, debe haber 10 procesos ejecutándose simultáneamente.
Por último, debe lanzarse el proceso 3.
Hay que tener presente que para que este proceso pueda funcionar correctamente deben estar todas las notas ya escritas.
Prueba a realizar el ejercicio haciendo uso de Pool y haciendo uso de bucles for.
"""