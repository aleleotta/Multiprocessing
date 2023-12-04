from multiprocessing import *
from random import randint
import time

def randomIp(connection):
    num1 = randint(0, 255)
    num2 = randint(0, 255)
    num3 = randint(0, 255)
    num4 = randint(0, 255)
    ip = str(num1)+"."+str(num2)+"."+str(num3)+"."+str(num4)
    pack = (ip, num1)
    connection.send(pack)
    connection.close()

def receiveIp(connection, connection1):
    pack = connection.recv()
    connection1.send(pack)
    connection.close()
    connection1.close()

def ipClassifier(connection):
    pack = connection.recv()
    ip, num1 = pack
    ipClass = "Class not identified"
    if num1 > 0 and num1 < 128:
        ipClass = "Class A"
    elif num1 >= 128 and num1 < 192:
        ipClass = "Class B"
    elif num1 >= 192 and num1 < 224:
        ipClass = "Class C"
    elif num1 >= 224 and num1 < 240:
        ipClass = "Class D"
    elif num1 >= 240 and num1 <= 255:
        ipClass = "Class E"
    else:
        ipClass = "Invalid IP"
    print(ip + " - " + ipClass)

if __name__ == "__main__":
    startTime = time.time()
    print("Time:" + str(startTime))
    left, right = Pipe()
    left1, right1 = Pipe()
    for i in range(1000):
        p1 = Process(target=randomIp, args=(left,))
        p2 = Process(target=receiveIp, args=(right, left1))
        p3 = Process(target=ipClassifier, args=(right1,))
        p1.start()
        p2.start()
        p3.start()

"""
En este ejercicio vamos a lanzar varios procesos, cuyas entradas y salidas están enlazadas.
Para ello tendremos tres procesos distintos:

    Proceso 1: Va a generar 10 direcciones IP de forma aleatoria y se las enviará al Proceso 2.
    Proceso 2: Va a leer las direcciones IP que recibe del Proceso 1 y
               va a enviar al Proceso 3 únicamente aquellas que pertenezcan a las clases A, B o C.
    Proceso 3: Va a leer las direcciones IP procedentes del Proceso 2 (no se sabe qué número llegarán)
               y va a imprimir por consola la dirección IP y a continuación la clase a la que pertenece.
	
    Lanza los tres procesos en orden.
"""