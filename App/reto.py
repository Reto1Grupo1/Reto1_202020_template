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
from statistics import mode



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




#FIN COMPARACIONES
#FUNCIONES PARA FILTRAR Y ORDENAR
def filtrar_por_genero(listadetails,name_gender):
    lista_genero=lt.newList("ARRAY_LIST")
    for i in range(1,lt.size(listadetails)+1):
             movie=lt.getElement(listadetails,i)
             genres=movie["genres"]
             genres=str(genres).split("|")
             if name_gender  in genres:
                lt.addLast(lista_genero,movie)  
    return lista_genero
def order_list(listadetails,parametro_average_best,parametro_average_worst,parametro_count_best,parametro_count_worst):
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
    for elemento in range(1, parametro_count_best+1):
        lt.addLast(countbest,lt.getElement(listadetails,elemento))


    sort.mergesort(listadetails,less_count)
    countworst=lt.newList("ARRAY_LIST")
    for elemento in range(1, parametro_count_worst+1):
        lt.addLast(countworst,lt.getElement(listadetails,elemento))
    return averagebest,averageworst,countbest,countworst
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

def loadMoviesDetails ():
    listadetails = loadCSVFile("Data/themoviesdb/SmallMoviesDetailsCleaned.csv") #llamar funcion cargar datos 
    print("Datos cargados details, ",lt.size(listadetails)," elementos cargados")
    return listadetails
def loadMoviesCasting():
    listacasting = loadCSVFile("Data/themoviesdb/MoviesCastingRaw-small.csv")
    print("Datos cargados casting, ",lt.size(listacasting)," elementos cargados")

    return listacasting


def create_ranking(listadetails, parametro_average_best,parametro_average_worst,parametro_count_best,parametro_count_worst):
    t1_start = process_time() #tiempo inicial
    try:
        averagebest,averageworst,countbest,countworst=order_list(listadetails, parametro_average_best,parametro_average_worst,parametro_count_best,parametro_count_worst)
        if parametro_average_best>0:
            print("-------------------------------------------------------------------")
            print("MEJOR VALORADAS")
        
        #print(averagebest)
            lista=[]
            x=lt.size(averagebest)
            print(x)
            for i in range(1,x+1):
                 y=lt.getElement(averagebest,i)
                 lista.append(y["original_title"])
            print (lista)
        if parametro_average_worst>0:
             print("-------------------------------------------------------------------")
             print("PEOR VALORADAS")
             lista=[]
             x=lt.size(averageworst)
             print(x)
             for i in range(1,x+1):
                 y=lt.getElement(averageworst,i)
                 lista.append(y["original_title"])
             print (lista)
        if parametro_count_best>0:
             print("-------------------------------------------------------------------")
             print("MEJOR VOTADAS")
             lista=[]
             #print(countbest)
             x=lt.size(countbest)
             print(x)
             for i in range(1,x+1):
                 y=lt.getElement(countbest,i)
                 lista.append(y["original_title"])
             print (lista)
        if parametro_count_worst>0:
             print("-------------------------------------------------------------------")
             print("PEOR VOTADAS")
             lista=[]
             x=lt.size(countworst)
             print(x)
             for i in range(1,x+1):
                 y=lt.getElement(countworst,i)
                 lista.append(y["original_title"])
             print (lista)
    except:
        print("Hubo un error al ingresar parametros, por favor vuelva a intentarlo.")
    t1_stop = process_time() #tiempo final
    print("-------------------------------------------------------------------")
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")

def know_director(director,listadetails,listacasting):
    t1_start = process_time() #tiempo inicia
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
        print("Error, nombre incorrecto. Intente de nuevo.")
    t1_stop = process_time() #tiempo final
    print("-------------------------------------------------------------------")
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    
def know_actor(actor,listadetails,listacasting):
    t1_start = process_time() #tiempo inicia
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
        print("Error, nombre incorrecto. Intente de nuevo.")
    t1_stop = process_time() #tiempo final
    print("-------------------------------------------------------------------")
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")


def understand_gender(listadetails,name_gender):
    t1_start = process_time() #tiempo inicial

    try:
         lista_genero=filtrar_por_genero(listadetails,name_gender)
         
         numero_peliculas= "Este género tiene "+str(lt.size(lista_genero))+" películas."
    #print(lista_genero)
         x=lt.size(lista_genero)
         sumatoria=0
         for i in range(1,x+1):
             y=lt.getElement(lista_genero,i)
             sumatoria+=float(y["vote_count"])
         print(numero_peliculas)
         print("-------------------------------------------------------------------")
         sumatoria_final="La cantidad de votos de este género es: "+ str(sumatoria)+" votos"
         print(sumatoria_final)
         print("-------------------------------------------------------------------")
         promedio = sumatoria/x
         promedio=round(promedio,2)
         promedio_final="El promedio de votos de este género es: " +str(promedio)+" votos"
         print(promedio_final)
    
    except:
        print("Género inválido, intente de nuevo.")
    t1_stop = process_time() #tiempo final
    print("-------------------------------------------------------------------")
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")


def create_ranking_gender(listadetails,name_gender,parametro_average_best,parametro_average_worst,parametro_count_best,parametro_count_worst):
     t1_start = process_time() #tiempo inicial

     try:
        lista_genero= filtrar_por_genero(listadetails,name_gender)
        averagebest,averageworst,countbest,countworst=order_list(lista_genero,parametro_average_best,parametro_average_worst,parametro_count_best,parametro_count_worst)
        x=lt.size(lista_genero)
        sumatoria=0
        for i in range(1,x+1):
             y=lt.getElement(lista_genero,i)
             sumatoria+=float(y["vote_count"])
        promedio = sumatoria/x
        promedio=round(promedio,2)
        promedio_final="El promedio de votos de de "+name_gender+" es : " +str(promedio)+" votos"
        print(promedio_final)
        sumatoria_average=0
        for i in range(1,x+1):
             y=lt.getElement(lista_genero,i)
             sumatoria_average+=float(y["vote_average"])
        promedio_average=sumatoria_average/x
        promedio=round(promedio_average,2)
        promedio_average_final="El promedio de calificaciones de las películas de "+name_gender+" es : " +str(promedio)+"."

        if parametro_average_best>0:
            print("-------------------------------------------------------------------")
            print("MEJOR VALORADAS: "+name_gender)
        
        #print(averagebest)
            lista=[]
            x=lt.size(averagebest)
            print(x)
            for i in range(1,x+1):
                 y=lt.getElement(averagebest,i)
                 lista.append(y["original_title"])
            print (lista)
        if parametro_average_worst>0:
             print("-------------------------------------------------------------------")
             print("PEOR VALORADAS: "+name_gender)
             lista=[]
             x=lt.size(averageworst)
             print(x)
             for i in range(1,x+1):
                 y=lt.getElement(averageworst,i)
                 lista.append(y["original_title"])
             print (lista)
             
        if parametro_count_best>0:
             print("-------------------------------------------------------------------")
             print("MEJOR VOTADAS: "+name_gender)
             lista=[]
             #print(countbest)
             x=lt.size(countbest)
             print(x)
             for i in range(1,x+1):
                 y=lt.getElement(countbest,i)
                 lista.append(y["original_title"])
             print (lista)
        if parametro_count_worst>0:
             print("-------------------------------------------------------------------")
             print("PEOR VOTADAS: "+name_gender)
             lista=[]
             x=lt.size(countworst)
             print(x)
             for i in range(1,x+1):
                 y=lt.getElement(countworst,i)
                 lista.append(y["original_title"])
             print (lista)
        print("-------------------------------------------------------------------")
        print(promedio_average_final)
        print("-------------------------------------------------------------------")
        print(promedio_final)
     except:
        print("Género inválido, intente de nuevo.")
     t1_stop = process_time() #tiempo final
     print("-------------------------------------------------------------------")
     print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    
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
                listacasting=loadMoviesCasting()
                listadetails=loadMoviesDetails()

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
                director=input("Escriba el nombre del director: ")
                know_director(director,listadetails,listacasting)


            elif int(inputs[0])==4: #opcion 4
                actor=input("Escriba el nombre del actor: ")
                know_actor(actor,listadetails,listacasting)

            elif int(inputs[0])==5: #opcion 5
                gender_name= input("Digite el nombre del género en inglés que desea entender:")
                understand_gender(listadetails,gender_name)

            elif int(inputs[0])==6: #opcion 6
                name_gender=input("¿Qué género desea rankear?")

                average_best=int(input("Desea ver las peliculas de  "+ name_gender +" mejor valoradas? 1: Si, 0: No: "))
                if average_best==1:
                            parametro_average_best=int(input("¿Cuántas películas mejor valoradas de "+ name_gender +" desea conocer?"))
                else:parametro_average_best=0
                average_worst=int(input("Desea ver las peliculas de  "+name_gender+ " peor valoradas? 1: Si, 0: No: "))
                if average_worst==1:
                            parametro_average_worst=int(input("¿Cuántas películas de "+name_gender+ " peor valoradas desea conocer?"))
                else: parametro_average_worst=0
                
                count_best=int(input("Desea ver las peliculas de "+name_gender+ " mejor votadas? 1: Si, 0: No: "))
                if count_best==1:
                            parametro_count_best=int(input("¿Cuántas películas de "+name_gender+" mejor votadas desea conocer?"))
                else: parametro_count_best=0


                count_worst=int(input("Desea ver las peliculas de  "+name_gender+ " peor votadas? 1: Si, 0: No: "))
                if count_worst==1:
                            parametro_count_worst=int(input("¿Cuántas películas de "+name_gender+ "peor votadas desea conocer?"))
                else:parametro_count_worst=0
                print(create_ranking_gender(listadetails,name_gender,parametro_average_best,parametro_average_worst,parametro_count_best,parametro_count_worst))

            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)
                
if __name__ == "__main__":
    main()