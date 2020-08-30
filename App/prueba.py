import config as cf
import sys
import csv

from ADT import list as lt
from DataStructures import listiterator as it
#from DataStructures import liststructure as lt
from Sorting import mergesort as sort
from time import process_time 
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
listadetails,listacasting=loadMovies()
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

def filtrar_por_genero(listadetails,name_gender):
    lista_genero=lt.newList("ARRAY_LIST")
    for i in range(1,lt.size(listadetails)+1):
             movie=lt.getElement(listadetails,i)
             genres=movie["genres"]
             genres=str(genres).split("|")
             if name_gender  in genres:
                lt.addLast(lista_genero,movie)  
    return lista_genero
lista_filtrada=filtrar_por_genero(listadetails,"Crime")
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


print (order_list(lista_filtrada,10,10,10,10))