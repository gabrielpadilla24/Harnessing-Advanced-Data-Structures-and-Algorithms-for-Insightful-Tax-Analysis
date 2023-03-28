"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
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
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert cf
from tabulate import tabulate
import traceback
default_limit = 1000 
sys.setrecursionlimit(default_limit*10)

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

data=''
def new_controller(estructura):
    """
        Se crea una instancia del controlador
    """
    control = controller.new_controller(estructura)
    return control

def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("0- Salir")


def load_data(maptype, porcentaje,sorting_method):
    """
    Carga los datos
    """
    nombre_archivo = ""
    if porcentaje==1:
       nombre_archivo = "Salida_agregados_renta_juridicos_AG-5pct.csv"
    elif porcentaje==2:  
        nombre_archivo = "Salida_agregados_renta_juridicos_AG-10pct.csv"
    elif porcentaje==3:  
        nombre_archivo = "Salida_agregados_renta_juridicos_AG-20pct.csv" 
    elif porcentaje==4:  
        nombre_archivo = "Salida_agregados_renta_juridicos_AG-30pct.csv"
    elif porcentaje==5:  
        nombre_archivo = "Salida_agregados_renta_juridicos_AG-50pct.csv"  
    elif porcentaje==6:  
        nombre_archivo = "Salida_agregados_renta_juridicos_AG-80pct.csv" 
    elif porcentaje==7:  
        nombre_archivo = "Salida_agregados_renta_juridicos_AG-large.csv"
    elif porcentaje==8:  
        nombre_archivo = "Salida_agregados_renta_juridicos_AG-small.csv"

    data = controller.load_data(maptype,nombre_archivo)
    numero_data=0
    for anio in range(2012,2022):
        anio=str(anio)
        dato=controller.get_data(data,anio)
        dato_anio=me.getValue(dato)
        lista_anio=dato_anio['Datos']
        lista_ordenada=controller.sort(lista_anio,sorting_method)
        primero_y_ultimo=controller.primeros_y_ultimos_Dat(lista_ordenada)
        numero_data=numero_data+lt.size(lista_ordenada)
        print(str(primero_y_ultimo))
        
    return data
        
    

def print_data(data, id):
    """
        Función que imprime un dato dado su ID
    """
    dato = controller.get_data(data, id)
    print("El dato con el ID", id, "es:", dato)

def print_req_1(data, anio, cod):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    print(tabulate(controller.req_1(data, anio, cod)[0], headers="keys",tablefmt="simple_grid", maxheadercolwidths=20, maxcolwidths=20))
    print("Tiempo tomado:", controller.req_1(data, anio, cod)[1], "ms.")
    print("Memoria utilizada:", controller.req_1(data, anio, cod)[2], "B.")
    print()


def print_req_2(data, anio, cod):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    print(tabulate(controller.req_2(data, anio, cod)[0], headers="keys",tablefmt="simple_grid", maxheadercolwidths=20, maxcolwidths=20))
    print("Tiempo tomado:", controller.req_2(data, anio, cod)[1], "ms.")
    print("Memoria utilizada:", controller.req_2(data, anio, cod)[2], "B.")
    print()
    #print(controller.req_2(data, anio, cod))


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(data, anio, cod):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    print(controller.req_2(data, anio, cod))


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    pass


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


# Se crea el controlador asociado a la vista
control = new_controller(estructura=1)
data=""
# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        try:
            
            if int(inputs) == 1:
                print("Ponga 1 si quiere de Maptype CHAINING")
                print("Ponga 2 si quiere de Maptype PROBING")
                maptype = int(input())
                print("Elija 1 si quiere cargar el archivo de tamaño 5%")
                print("Elija 2 si quiere cargar el archivo de tamaño 10%")
                print("Elija 3 si quiere cargar el archivo de tamaño 20%")
                print("Elija 4 si quiere cargar el archivo de tamaño 30%")
                print("Elija 5 si quiere cargar el archivo de tamaño 50%")
                print("Elija 6 si quiere cargar el archivo de tamaño 80%")
                print("Elija 7 si quiere cargar el archivo de tamaño -large")
                print("Elija 8 si quiere cargar el archivo de tamaño -small")
                porcentaje = int(input())
                print("Presione 1 si desea que se ordenen los datos mediante Selection sort")
                print("Presione 2 si desea que se ordenen los datos mediante Insertion sort")
                print("Presione 3 si desea que se ordenen los datos mediante Shell sort")
                print("Presione 4 si desea que se ordenen los datos mediante Quick sort")
                print("Presione 5 si desea que se ordenen los datos mediante Merge sort")
                tipo_algo=int(input())
                
                print("Cargando información de los archivos ....\n")
                data=load_data(maptype,porcentaje,tipo_algo)
                print("Total de lineas de datos cargadas:  ")
                
                x = 3
                width = [20]
                #width = width*data    
                
                print("Los primeros ", x, "datos cargados son: ")
                print()
                
                print("Los últimos ", x, "datos cargados son: ")
            
                
                
               
                
            elif int(inputs) == 2:
                anio = input("Año a consultar:")
                cod = input("Código de sector económico a consultar:")
                (print_req_1(data, anio, cod))
                

            elif int(inputs) == 3:
                anio = input("Año a consultar: ")
                cod = input("Código de sector económico a consultar: ")
                (print_req_2(data, anio, cod))
                #print('Escriba el año que desea consultar: ')
                #anio = input()
                #print('Escriba el codigo que desea consultar: ')
                #cod = input() 
                #print_req_2(data, anio, cod)
                #print(data)

            elif int(inputs) == 4:
                print_req_3(control)

            elif int(inputs) == 5:
                anio = input('Año a consultar: ')
                cod = input('Código de sector económico a consultar: ')
                print_req_4(data,anio, cod)

            elif int(inputs) == 6:
                print_req_5(control)

            elif int(inputs) == 7:
                print_req_6(control)

            elif int(inputs) == 8:
                print_req_7(control)

            elif int(inputs) == 9:
                print_req_8(control)

            elif int(inputs) == 0:
                working = False
                print("\nGracias por utilizar el programa")
                
            elif int(inputs) == 11:
                print_data(data, input())                
            else:
                print("Opción errónea, vuelva a elegir.\n")
        except Exception as exp:
            print("ERR:", exp)
            traceback.print_exc()
    sys.exit(0)
