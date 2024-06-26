﻿"""
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


def load_data(maptype, porcentaje,sorting_method,Memoria):
    """
    Carga los datos
    """
    resp=None
    if Memoria=='True':
        Memoria=True
    elif Memoria == 'False':
        Memoria==False
        
    if Memoria==True:
        controller.tracemalloc_start()
        memoria=controller.get_memory()
        
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
    lista2 = lt.newList()
    for anio in range(2012,2022):
        anio=str(anio)
        dato=controller.get_data(data,anio)
        dato_anio=me.getValue(dato)
        lista_anio=dato_anio['Datos']
        lista_ordenada=controller.sort(lista_anio,sorting_method)
        primero_y_ultimo=controller.primeros_y_ultimos_Dat(lista_ordenada)
        lt.addLast(lista2, primero_y_ultimo)
        numero_data=numero_data+lt.size(lista_ordenada)

    PyUiterable = lt.iterator(lista2)

    if Memoria==True:
        memoria2=controller.get_memory() 
        controller.tracemalloc_end()
        memoria_total=controller.delta_memory(memoria,memoria2)
        memoria_total=round(memoria_total,2)
        resp=('La memoria total es:'+str(memoria_total)+' KB')
        
    return data,resp,PyUiterable
        
    

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


def print_req_4(data, anio):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """

    # TODO: Imprimir el resultado del requerimiento 4

    respuestas = controller.req_4(data, anio)
    respuesta_1 = respuestas[0]

    l_respuesta1 = len(respuesta_1)

     # timempo
    #l_respuesta1 = len(controller.req_4(data, anio))
    #respuesta_1 = controller.req_4(data, anio)

    if l_respuesta1 != 9:
        tabla = respuesta_1[0]
        print('========== Req No. 4 Answer ==========')
        print(f'El tiempo de ejecución es {respuestas[1]} ms')
        print(f'El subsector económico con mayores costos y gastos de nómina para el año {anio}')
        table_data = [
            ['Código sector económico', 'Nombre sector económico', 'Código Subsector Económico', 'Nombre subsector económico', 'Total de Costos y gastos nómina del subsector económico', 'Total ingresos netos del subsector económico', 'Total Costos y Gastos del subsector económico', 'Total saldo a pagar del subsector económico', 'Total saldo a favor del subsector económico'],
            [tabla['Código sector económico'], tabla['Nombre sector económico'], tabla['Código Subsector Económico'], tabla['Nombre subsector económico'], tabla['Total de Costos y gastos nómina del subsector económico'], tabla['Total ingresos netos del subsector económico'], tabla['Total Costos y Gastos del subsector económico'], tabla['Total saldo a pagar del subsector económico'], tabla['Total saldo a favor del subsector económico']]   
        ]
        print(tabulate(table_data, headers='firstrow', tablefmt='fancy_grid'))

        top1, top2, top3, peor1, peor2, peor3 = respuesta_1[3], respuesta_1[2], respuesta_1[1], respuesta_1[4], respuesta_1[5], respuesta_1[6]

        print('')
        print('Las 3 actividades económicas que más aportaron al valor total de costos y gastos de nómina del subsector son: ')
        print('')
        tabla1 = [
            ['Código Actividad económica', 'Nombre Actividad Económica', 'Costos y gastos nómina', 'El total de ingresos netos', 'El total de costos y gastos', 'El total de saldo a pagar','El total de saldo a favor'],
            [top1['Código Actividad económica'],top1['Nombre Actividad Económica'],top1['Costos y gastos nómina'],top1['El total de ingresos netos'],top1['El total de costos y gastos'],top1['El total de saldo a pagar'],top1['El total de saldo a favor']],
            [top2['Código Actividad económica'],top2['Nombre Actividad Económica'],top2['Costos y gastos nómina'],top2['El total de ingresos netos'],top2['El total de costos y gastos'],top2['El total de saldo a pagar'],top2['El total de saldo a favor']],
            [top3['Código Actividad económica'],top3['Nombre Actividad Económica'],top3['Costos y gastos nómina'],top3['El total de ingresos netos'],top3['El total de costos y gastos'],top3['El total de saldo a pagar'],top3['El total de saldo a favor']]
        ]
        print(tabulate(tabla1, headers='firstrow', tablefmt='fancy_grid'))

        print('')
        print('Las 3 actividades económicas que menos aportaron al valor total de costos y gastos de nómina del subsector son: ')
        print('')
        tabla2 = [
            ['Código Actividad económica', 'Nombre Actividad Económica', 'Costos y gastos nómina', 'El total de ingresos netos', 'El total de costos y gastos', 'El total de saldo a pagar','El total de saldo a favor'],
            [peor1['Código Actividad económica'],peor1['Nombre Actividad Económica'],peor1['Costos y gastos nómina'],peor1['El total de ingresos netos'],peor1['El total de costos y gastos'],peor1['El total de saldo a pagar'],peor1['El total de saldo a favor']],
            [peor2['Código Actividad económica'],peor2['Nombre Actividad Económica'],peor2['Costos y gastos nómina'],peor2['El total de ingresos netos'],peor2['El total de costos y gastos'],peor2['El total de saldo a pagar'],peor2['El total de saldo a favor']],
            [peor3['Código Actividad económica'],peor3['Nombre Actividad Económica'],peor3['Costos y gastos nómina'],peor3['El total de ingresos netos'],peor3['El total de costos y gastos'],peor3['El total de saldo a pagar'],peor3['El total de saldo a favor']]
        ]

        print(tabulate(tabla2, headers='firstrow', tablefmt='fancy_grid'))  
      
    else:
        tabla = respuesta_1
        print('========== Req No. 4 Answer ==========')
        print(f'El tiempo de ejecución es {respuestas[1]} ms!')
        print(f'El subsector económico con mayores costos y gastos de nómina para el año {anio}')

        
        table_data = [
            ['Código sector económico', 'Nombre sector económico', 'Código Subsector Económico', 'Nombre subsector económico', 'Total de Costos y gastos nómina del subsector económico', 'Total ingresos netos del subsector económico', 'Total Costos y Gastos del subsector económico', 'Total saldo a pagar del subsector económico', 'Total saldo a favor del subsector económico'],
            [tabla['Código sector económico'], tabla['Nombre sector económico'], tabla['Código Subsector Económico'], tabla['Nombre subsector económico'], tabla['Total de Costos y gastos nómina del subsector económico'], tabla['Total ingresos netos del subsector económico'], tabla['Total Costos y Gastos del subsector económico'], tabla['Total saldo a pagar del subsector económico'], tabla['Total saldo a favor del subsector económico']]    
        ]
        print(tabulate(table_data, headers='firstrow', tablefmt='fancy_grid'))

        print('Hay menos de 6 actividades económicas')

           
    


def print_req_5(data,anio):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    x=controller.req_5(data,anio)
   
    return x


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass


def print_req_7(data,anio,cod,n_actividades):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    anio=str(anio)
    cod=str(cod)
    print(controller.req_7(data,anio,cod,n_actividades))


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
                print('Escriba True si quiere saber la memoria o False si no quiere saberla')
                memoria=input()
                print("Cargando información de los archivos ....\n")
                resp=load_data(maptype,porcentaje,tipo_algo,memoria)
                data=resp[0]
                print("Los primeros y ultimos 3 datos cargados por año son: ")
                print()
                for anio in resp[2]:
                    for elem in lt.iterator(anio):
                        print("dato")
                        print(tabulate(elem, headers="keys",tablefmt="simple_grid", maxheadercolwidths=20))

                if resp[1]!=None:
                    print(resp[1])
                print("Total de lineas de datos cargadas:  ")
                
        
                
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
                print_req_4(data,anio)

            elif int(inputs) == 6:
                print('Escriba el año del que quiere saber el subsector económico que tuvo los mayores descuentos tributarios y las tres actividades economicas que menos y mas aportarona este')
                anio=int(input())
                anio=str(anio)
                x=print_req_5(data,anio)
                print('El subsector con mayores mayores descuentostributarios')
                print(x[0][0])
                print()
                print('Las tres actividades económicas que menos aportaron y las tres actividades económicas que más aportaron al valor total de Descuentos tributarios del subsector son')
                print(x[0][1])
                print('El tiempo que de carga fue:'+str(x[1]))

            elif int(inputs) == 7:
                print_req_6(control)

            elif int(inputs) == 8:
                print('Escriba el numero de actividades económicas a identificar')
                n_actividades=input()
                print('Escriba el Año a consultar')
                anio=input()
                print('Escriba el Código de subsector económico a identificar')
                cod=input()
                print_req_7(data,anio,cod,n_actividades)

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
