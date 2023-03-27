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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """

import csv
import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
import os
assert cf


"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos
def comp_anio(dato_1,dato_2):
    anio1=dato_1
    anio2=me.getKey(dato_2)
    
    if int(anio1)>int(anio2):
        return 1
    elif int(anio1)<int(anio2):
        return -1
    elif int(anio1)==int(anio2):
        return 0

def new_data_structs(maptype):
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    
    if maptype == 1:
        # config ADT Map as CHAINING
        dian_mp = mp.newMap(1000,
                               maptype="CHAINING",
                               loadfactor=4.0,
                               cmpfunction=comp_anio)
        return dian_mp
    if maptype == 2:
        # config ADT Map as PROBING
        dian_mp = mp.newMap(1000,
                               maptype="PROBING",
                               loadfactor=0.5,
                               cmpfunction=comp_anio)
        return dian_mp

   


# Funciones para agregar informacion al modelo

def newYear(year):
    entry = {'year': "", "tax": None}
    entry['year'] = year
    entry['tax'] = lt.newList('SINGLE_LINKED', cmpYears)
    return entry

def add_data(mapa_vacio,info):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    
    mp.put(mapa_vacio,info['Año'],info)
    return mapa_vacio

    


# Funciones para creacion de datos

def put_Dian(mapa_vacio,info):
    mp.put(mapa_vacio,info['Año'],info)
    return mapa_vacio

def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    pass


# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    return mp.size(data_structs['Años'])


def req_1(data):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1

    pass
    
    


def req_2(data, anio, cod):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    x = mp.size(data)
    y = mp.get(data, '2012')
    
    #return x, anio, cod
    return x


def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    pass


def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass


def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    pass

# Funciones de ordenamiento


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    pass

def cmpYears(year1, year2):
    if (int(year1) == int(year2)):
        return 0
    elif (int(year1) > int(year2)):
        return 1
    else:
        return -1
    

def cmpMapTaxAnio(entry_1, entry_2):
    
    yearentry = me.getKey(entry_2)
    if entry_1 < yearentry:
        return 1
    elif entry_1 == yearentry:
        return 0
    else:
        return -1


def sort(data_structs, tipo_algo):
    """
    Función encargada de ordenar la lista con los datos
    """
    if tipo_algo == 1:
        return se.sort(data_structs["data"], sort_criteria)
    
    if tipo_algo == 2:
        return ins.sort(data_structs["data"], sort_criteria)
    
    if tipo_algo == 3:
        return sa.sort(data_structs["data"], sort_criteria)
    
    if tipo_algo ==4:
        return quk.sort(data_structs["data"], sort_criteria)
    
    if tipo_algo ==5:
        return merg.sort(data_structs["data"], sort_criteria)
