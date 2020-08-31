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
from DataStructures import liststructure as lt
from statistics import mode
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
    return False

def greater_count(element1, element2):
    if float(element1['vote_count']) > float(element2['vote_count']):
        return True
    return False

def less_count(element1, element2):
    if float(element1['vote_count']) < float(element2['vote_count']):
        return True
    return False

def loadCSVFile (file, cmpfunction):
    lst=lt.newList("SINGLE_LINKED", cmpfunction)
    dialect = csv.excel()
    dialect.delimiter=";"
    try:
        with open(  cf.data_dir + file, encoding="utf-8") as csvfile:
            row = csv.DictReader(csvfile, dialect=dialect)
            for elemento in row: 
                lt.addLast(lst,elemento)
    except:
        print("Hubo un error con la carga del archivo")
    return lst


def loadMoviesDetails ():
    listadetails = loadCSVFile("theMoviesdb/SmallMoviesDetailsCleaned.csv",compareRecordIds) 
    print("Datos cargados, " + str(lt.size(listadetails)) + " elementos cargados")
    return listadetails

def loadMoviesCasting ():
    listacasting = loadCSVFile("theMoviesdb/MoviesCastingRaw-small.csv",compareRecordIds) 
    print("Datos cargados, " + str(lt.size(listacasting)) + " elementos cargados")
    return listacasting

def requerimiento3(director,listadetails,listacasting):
    try:
        listapeliculas=lt.newList("ARRAY_LIST")
        listaid=lt.newList("ARRAY_LIST")
        totalpeliculas=0
        calificacion=0

        for i in range(1,int(lt.size(listacasting))+1):
            a=(lt.getElement(listacasting,i))["id"]
            if (lt.getElement(listacasting,i))["director_name"] == director:
                lt.addLast(listaid,a)
        for i in range(1,(lt.size(listaid))+1):
            for j in range(1,int(lt.size(listadetails))+1):
                if str(lt.getElement(listaid,i))==str((lt.getElement(listadetails,j))["id"]):
                    lt.addLast(listapeliculas,(lt.getElement(listadetails,j))["title"])
                    totalpeliculas+=1
                    calificacion+=float((lt.getElement(listadetails,j))["vote_average"])

        promedio=calificacion/totalpeliculas

        print("Peliculas del director: ")
        for i in range(1,(lt.size(listapeliculas))+1):
            print(lt.getElement(listapeliculas,i))
        print("-------------------------------------------------------------------")
        print("Numero de peliculas del director: "+str(totalpeliculas))
        print("-------------------------------------------------------------------")
        print("Promedio de calificacion de peliculas: "+str(round(promedio,2)))

    except:
        print("Error, nombre erroneo")
    
def requerimiento4(actor,listadetails,listacasting):
    try:
        listapeliculas=lt.newList("ARRAY_LIST")
        listaid=lt.newList("ARRAY_LIST")
        totalpeliculas=0
        calificacion=0
        listadirectores=[]

        for i in range(1,int(lt.size(listacasting))+1):
            a=(lt.getElement(listacasting,i))["id"]
            if (lt.getElement(listacasting,i))["actor1_name"] == actor:
                lt.addLast(listaid,a)
                listadirectores.append((lt.getElement(listacasting,i))["director_name"])
            elif (lt.getElement(listacasting,i))["actor2_name"] == actor:
                lt.addLast(listaid,a)
                listadirectores.append((lt.getElement(listacasting,i))["director_name"])
            elif (lt.getElement(listacasting,i))["actor3_name"] == actor:
                lt.addLast(listaid,a)
                listadirectores.append((lt.getElement(listacasting,i))["director_name"])
            elif (lt.getElement(listacasting,i))["actor4_name"] == actor:
                lt.addLast(listaid,a)
                listadirectores.append((lt.getElement(listacasting,i))["director_name"])
            elif (lt.getElement(listacasting,i))["actor5_name"] == actor:
                lt.addLast(listaid,a)
                listadirectores.append((lt.getElement(listacasting,i))["director_name"])

        for i in range(1,(lt.size(listaid))+1):
            for j in range(1,int(lt.size(listadetails))+1):
                if str(lt.getElement(listaid,i))==str((lt.getElement(listadetails,j))["id"]):
                    lt.addLast(listapeliculas,(lt.getElement(listadetails,j))["title"])
                    totalpeliculas+=1
                    calificacion+=float((lt.getElement(listadetails,j))["vote_average"])

        promedio=calificacion/totalpeliculas

        director=mode(listadirectores)

        print("Peliculas del actor: ")
        for i in range(1,(lt.size(listapeliculas))+1):
            print(lt.getElement(listapeliculas,i))
        print("-------------------------------------------------------------------")
        print("Numero de peliculas del actor: "+str(totalpeliculas))
        print("-------------------------------------------------------------------")
        print("Promedio de calificacion de peliculas: "+str(round(promedio,2)))
        print("-------------------------------------------------------------------")
        print("Director con mas peliculas: "+str(director))

    except:
        print("Error, nombre erroneo")

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
                listadetails = loadMoviesDetails ()
                listacasting = loadMoviesCasting ()
            elif int(inputs[0])==2: #opcion 2
                pass

            elif int(inputs[0])==3: #opcion 3
                director=input("Escriba el nombre del director: ")
                requerimiento3(director,listadetails,listacasting)

            elif int(inputs[0])==4: #opcion 4
                actor=input("Escriba el nombre del actor: ")
                requerimiento4(actor,listadetails,listacasting)

            elif int(inputs[0])==3: #opcion 5
                pass

            elif int(inputs[0])==4: #opcion 6
                pass


            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)
                
if __name__ == "__main__":
    main()