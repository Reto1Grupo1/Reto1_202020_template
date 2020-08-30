"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 * Contribución de:
 *
 * Cristian Camilo Castellanos
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

"""
  Este módulo es una aplicación básica con un menú de opciones para cargar datos, contar elementos, y hacer búsquedas sobre una lista .
"""

import config as cf
import sys
import csv

from ADT import list as lt
from DataStructures import listiterator as it
#from DataStructures import liststructure as lt
from Sorting import mergesort as sort
from time import process_time 



def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Ranking de peliculas")
    print("3- Conocer un director")
    print("4- Conocer un actor")
    print("5- Entender un genero")
    print("6- Crear ranking")
    print("0- Salir")


#COMPARACIONES

def compareRecordIds (recordA, recordB):
    if int(recordA['id']) == int(recordB['id']):
        return 0
    elif int(recordA['id']) > int(recordB['id']):
        return 1
    return -1
def greater_average(element1, element2):
    if float(element1['vote_average']) > float(element2['vote_average']):
        return True
    return False
def less_average(element1, element2):
    if float(element1['vote_average']) < float(element2['vote_average']):
        return True



def greater_count(element1, element2):
    if float(element1['vote_count']) > float(element2['vote_count']):
        return True
    return False
def less_count(element1, element2):
    if float(element1['vote_count']) < float(element2['vote_count']):
        return True

def crear_lista(element1, element2):
    lista=[]
    if (element1['original_title']) < (element2['original_title']):
            append.lista(element1["original_title"])
    return lista
#FIN COMPARACIONES
def loadCSVFile (file, sep=";"):

    #lst = lt.newList("ARRAY_LIST") #Usando implementacion arraylist
    lst = lt.newList("SINGLE_LINKED") #Usando implementacion linkedlist
    print("Cargando archivo ....")
    t1_start = process_time() #tiempo inicial
    dialect = csv.excel()
    dialect.delimiter=sep
    try:
        with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                lt.addLast(lst,row)
    except:
        print("Hubo un error con la carga del archivo")
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return lst

def loadMovies ():
    
    listadetails = loadCSVFile("Data/themoviesdb/SmallMoviesDetailsCleaned.csv") #llamar funcion cargar datos
    listacasting = loadCSVFile("Data/themoviesdb/MoviesCastingRaw-small.csv")
    print("Datos cargados details, ",lt.size(listadetails)," elementos cargados")
    print("Datos cargados casting, ",lt.size(listacasting)," elementos cargados")
    

    return listadetails,listacasting


def create_ranking(listadetails, parametro_average_best,parametro_average_worst,parametro_count_best,parametro_count_worst):
    sort.mergesort(listadetails,greater_average)
    averagebest=lt.newList("ARRAY_LIST") #Usando implementacion linkedlist
    for elemento in range(1,parametro_average_best+1):
        lt.addLast(averagebest,lt.getElement(listadetails,elemento))

    averageworst= lt.newList("ARRAY_LIST")
    sort.mergesort(listadetails,less_average)
    for elemento in range(1,parametro_average_worst+1):
        lt.addLast(averageworst,lt.getElement(listadetails,elemento))


    sort.mergesort(listadetails,greater_count)
    countbest=lt.newList("ARRAY_LIST")
    for elemento in range(1, parametro_average_best+1):
        lt.addLast(countbest,lt.getElement(listadetails,elemento))


    sort.mergesort(listadetails,less_count)
    countworst=lt.newList("ARRAY_LIST")
    for elemento in range(0, parametro_average_worst+1):
        lt.addLast(countworst,lt.getElement(listadetails,elemento))
    
    
    if parametro_average_best>0:
        print("-------------------------------------------------------------------")
        print("MEJOR VALORADAS")
        
        print(averagebest)
        lista=[]
        for i in range(1,11):
            # lista.append(averagebest["elements"][i]["original_title"])
        print(len(averagebest))
        print (lista)
    if parametro_average_worst>0:
        print("-------------------------------------------------------------------")
        print("PEOR VALORADAS")
        print(averageworst)
    if parametro_count_best>0:
        print("-------------------------------------------------------------------")
        print("MEJOR VOTADAS")
        print(countbest)
    if parametro_count_worst>0:
        print("-------------------------------------------------------------------")
        print("PEOR VOTADAS")
        print(countworst)
def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """


    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada
        if len(inputs)>0:

            if int(inputs[0])==1: #opcion 1
                listadetails,listacasting = loadMovies()
                
            elif int(inputs[0])==2: #opcion 2
                average_best=int(input("Desea ver las peliculas mejor valoradas? 1: Si, 0: No: "))
                if average_best==1:
                            parametro_average_best=int(input("¿Cuántas películas mejor valoradas desea conocer?"))
                else:parametro_average_best=0
                average_worst=int(input("Desea ver las peliculas peor valoradas? 1: Si, 0: No: "))
                if average_worst==1:
                            parametro_average_worst=int(input("¿Cuántas películas peor valoradas desea conocer?"))
                else: parametro_average_worst=0
                
                count_best=int(input("Desea ver las peliculas mejor votadas? 1: Si, 0: No: "))
                if count_best==1:
                            parametro_count_best=int(input("¿Cuántas películas mejor votadas desea conocer?"))
                else: parametro_count_best=0


                count_worst=int(input("Desea ver las peliculas peor votadas? 1: Si, 0: No: "))
                if count_worst==1:
                            parametro_count_worst=int(input("¿Cuántas películas peor votadas desea conocer?"))
                else:parametro_count_worst=0
                print(create_ranking(listadetails, parametro_average_best,parametro_average_worst,parametro_count_best,parametro_count_worst))


            elif int(inputs[0])==3: #opcion 3
                pass

            elif int(inputs[0])==4: #opcion 4
                print(comparador(listadetails))

            elif int(inputs[0])==3: #opcion 5
                pass

            elif int(inputs[0])==4: #opcion 6
                pass


            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)
                
if __name__ == "__main__":
    main()