from multiprocessing import *

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