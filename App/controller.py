"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
import model
import time
import csv
import tracemalloc
import os

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""



def new_controller(estructura):
    """
    Crea una instancia del modelo
    """
    control = {
        "model": None
    }
    if estructura ==1:
        TipoAbsEstructura = "PROBING"
    else:
        TipoAbsEstructura = "CHAINING"
        
    control["model"] = model.new_data_structs(TipoAbsEstructura)
    return control


# Funciones para la carga de datos

def load_data(maptype, nombre_archivo):
    """
    Carga los datos del reto
    """
    mapa = model.new_data_structs(maptype)
    name = cf.data_dir + nombre_archivo
    archivo = csv.DictReader(open(name, encoding='utf-8'))

    for anios in archivo:
        model.add_data(mapa,anios['Año'], anios)
        
    return mapa
    
    
    


# Funciones de ordenamiento

def sort(control, tipo_algo):
    """
    Ordena los datos del modelo
    """
    
    x=model.sort(control, tipo_algo)

    return x


# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    data = model.get_data(control, id)
    return data

def primeros_y_ultimos_Dat(list):
    x=model.primeros_y_ultimos_Dat(list)
    return x


def ultimos_x_datos(control, amount, size):
    """
    Retorna una lista de los ultimos amount datos cargados
    """
    i = size
    indexes = i - amount
    data = []
    while indexes < i:
        data.append(get_data(control, indexes))
        indexes = indexes + 1
        
    return data


def req_1(data, anio, cod):
    """
    Retorna el resultado del requerimiento 1
    """
    
    
    start_memory = get_memory()
    start = get_time()
    returnable = model.req_1(data, anio, cod)
    stop = get_time()
    stop_memory = get_memory()
    memory = delta_memory(stop_memory, start_memory)
    time = delta_time(start, stop)

    return (returnable, time, memory)



def req_2(data, anio, cod):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    start_memory = get_memory()
    start = get_time()
    returnable = model.req_2(data, anio, cod)
    stop = get_time()
    stop_memory = get_memory()
    memory = delta_memory(stop_memory, start_memory)
    time = delta_time(start, stop)

    return (returnable, time, memory)


def req_3(control):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(data, anio):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    return model.req_4(data, anio)


def req_5(control):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(control):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


def req_7(control):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass


def req_8(control):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed

def get_memory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    tracemalloc.start()
    tracemalloc.clear_traces()
    return tracemalloc.take_snapshot()


def delta_memory(stop_memory, start_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory
