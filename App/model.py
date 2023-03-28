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

def primeros_y_ultimos_Dat(list):
    lista=lt.newList()
    primeros=lt.subList(list,1,3)
    ultimo=lt.subList(list,lt.size(list)-2,3)
    primeros_iterando=lt.iterator(primeros)
    ultimos_iterando=lt.iterator(ultimo)
    
    for i in primeros_iterando:
        lt.addLast(lista,i)
    for i in ultimos_iterando:
        lt.addFirst(lista,i)
    return lista

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
    entry = {'Year': "", "Datos": None}
    entry['Year'] = year
    entry['Datos'] = lt.newList('SINGLE_LINKED')
    return entry

def add_data(mapa,anio,info):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    authors = mapa
    existauthor = mp.contains(authors, anio)
    if existauthor:
        entry = mp.get(authors, anio)
        author = me.getValue(entry)
    else:
        author = newYear(anio)
        mp.put(authors, anio, author)
    lt.addLast(author['Datos'], info)
    

    


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
    x=mp.get(data_structs,id)
    return x


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    return mp.size(data_structs['Años'])


def req_1(data, anio, cod):
    """
    Función que soluciona el requerimiento 1
    """
    datoanio = get_data(data, anio)
    
    valores = lt.newList()
    
    datositerables = lt.iterator(me.getValue(datoanio)["Datos"])
    
    for taxroll in datositerables:
        if taxroll["Código sector económico"] == cod:
            lt.addLast(valores, taxroll)
    
    valores = se.sort(valores, cmpMapSaldoPagar)
    maxsaldo = lt.firstElement(valores)
    
    keys = lt.newList()
    [lt.addLast(keys, i) for i in ["Código actividad económica","Nombre actividad económica","Código subsector económico","Nombre subsector económico","Total ingresos netos", "Total costos y gastos", "Total saldo a pagar","Total saldo a favor"]]
    values = lt.newList()
    
    for element in lt.iterator(keys):
        lt.addLast(values, [maxsaldo[element]])
        
    returnable = dict(zip(lt.iterator(keys),lt.iterator(values)))
        
    
    return returnable
    


def req_2(data, anio, cod):
    """
    Función que soluciona el requerimiento 2
    """
    datoanio = get_data(data, anio)
    
    valores = lt.newList()
    
    datositerables = lt.iterator(me.getValue(datoanio)["Datos"])
    
    for taxroll in datositerables:
        if taxroll["Código sector económico"] == cod:
            lt.addLast(valores, taxroll)
    
    valores = se.sort(valores, cmpMapSaldoaFavor)
    maxsaldo = lt.firstElement(valores)
    
    keys = lt.newList()
    [lt.addLast(keys, i) for i in ["Código actividad económica","Nombre actividad económica","Código subsector económico","Nombre subsector económico","Total ingresos netos", "Total costos y gastos", "Total saldo a pagar","Total saldo a favor"]]
    values = lt.newList()
    
    for element in lt.iterator(keys):
        lt.addLast(values, [maxsaldo[element]])
        
    returnable = dict(zip(lt.iterator(keys),lt.iterator(values)))
        
    
    return returnable


def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    pass


def req_4(data, anio):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    datoanio = get_data(data, anio)
    
    subsectores = {}
    
    datositerables = lt.iterator(me.getValue(datoanio)["Datos"])
    
    for taxroll in datositerables:
        subsector = taxroll["Código subsector económico"]
        if subsector in subsectores:
            subsectores[subsector] += int(taxroll["Costos y gastos nómina"])
        else:
            subsectores[subsector] = int(taxroll["Costos y gastos nómina"])
    
    sorted_subsectores = sorted(subsectores.items(), key=lambda x: x[1], reverse=True)
    max_subsector = sorted_subsectores[0][0]
    
    info_subsector = obtener_informacion_subsector(data, anio, max_subsector)
    
    return {
        'Código Subsector Económico': max_subsector,
        'Código sector económico': info_subsector['Código sector económico'],
        'Nombre sector económico': info_subsector['Nombre sector económico'],
        'Nombre subsector económico': info_subsector['Nombre subsector económico'],
        'Costos y gastos nómina': info_subsector['Costos y gastos nómina'],
        'Total Costos y Gastos': info_subsector['Total costos y gastos'],
        'Total ingresos netos': info_subsector['Total ingresos netos'],
        'Total saldo a pagar' : info_subsector['Total saldo a pagar'],
        'Total saldo a favor': info_subsector['Total saldo a favor']
    }

    

def obtener_informacion_subsector(data, anio, cod_subsector):
    """
    Función que devuelve la información del subsector económico dado en el año dado.
    """
    datoanio = get_data(data, anio)
    datositerables = lt.iterator(me.getValue(datoanio)["Datos"])
    
    codigo_sector = None
    nombre_sector = None
    nombre_subsector = None
    total_cyg_nomina = 0
    total_ingresos_netos = 0
    total_costos_gastos = 0
    total_saldo_por_pagar = 0
    total_saldo_favor = 0
    
    for taxroll in datositerables:
        if taxroll["Código subsector económico"] == cod_subsector:
            if not codigo_sector:
                codigo_sector = taxroll["Código sector económico"]
                nombre_sector = taxroll["Nombre sector económico"]
                nombre_subsector = taxroll["Nombre subsector económico"]
                total_cyg_nomina += int(taxroll['Costos y gastos nómina'])
                total_costos_gastos += int(taxroll["Total costos y gastos"])
                total_ingresos_netos += int(taxroll['Total ingresos netos'])
                total_saldo_por_pagar += int(taxroll['Total saldo a pagar'])
                total_saldo_favor += int(taxroll['Total saldo a favor'])
    return {
        'Código sector económico': codigo_sector,
        'Nombre sector económico': nombre_sector,
        'Código subsector económico': cod_subsector,
        'Nombre subsector económico': nombre_subsector,
        'Costos y gastos nómina': total_cyg_nomina,
        'Total costos y gastos' : total_costos_gastos,
        'Total ingresos netos': total_ingresos_netos,
        'Total saldo a pagar' : total_saldo_por_pagar,
        'Total saldo a favor': total_saldo_favor
        
    }





''''
def req_4(data, anio):
    """
    Función que devuelve el subsector económico con mayores costos y gastos de nómina para un año dado
    """
    datoanio = get_data(data, anio)
    
    subsectores = {}
    
    datositerables = lt.iterator(me.getValue(datoanio)["Datos"])
    
    for taxroll in datositerables:
        subsector = taxroll["Código subsector económico"]
        if subsector in subsectores:
            subsectores[subsector] += int(taxroll["Total costos y gastos de nómina"])
        else:
            subsectores[subsector] = int(taxroll["Total costos y gastos de nómina"])
    
    sorted_subsectores = sorted(subsectores.items(), key=lambda x: x[1], reverse=True)
    max_subsector = sorted_subsectores[0][0]
    
    # obtener información del subsector con mayores costos y gastos de nómina
    info_subsector = obtener_informacion_subsector(data, anio, max_subsector)
    
    return {
        'codigo_subsector_economico': max_subsector,
        'codigo_sector_economico': info_subsector['codigo_sector_economico'],
        'nombre_sector_economico': info_subsector['nombre_sector_economico'],
        'nombre_subsector_economico': info_subsector['nombre_subsector_economico']
    }
'''


    



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
    
    
    if entry_1['Código actividad económica']< entry_2['Código actividad económica']:
        return True
    else:
        return False
    
def cmpMapSaldoPagar(entry_1, entry_2):
    
    
    if int(entry_1['Total saldo a pagar'])> int(entry_2['Total saldo a pagar']):
        return True
    else:
        return False
    
def cmpMapSaldoaFavor(entry_1, entry_2):
    if int(entry_1['Total saldo a favor'])> int(entry_2['Total saldo a favor']):
        return True
    else:
        return False
    
def cmpMapCostosGN(entry_1, entry_2):
    if int(entry_1['Costos y gastos nómina']) > int(entry_2['Costos y gastos nómina']):
        return True
    else:
        return False



def sort(data_structs, tipo_algo):
    """
    Función encargada de ordenar la lista con los datos
    """
    if tipo_algo == 1:
        return se.sort(data_structs, cmpMapTaxAnio)
    
    if tipo_algo == 2:
        return ins.sort(data_structs, cmpMapTaxAnio)
    
    if tipo_algo == 3:
        return sa.sort(data_structs, cmpMapTaxAnio)
    
    if tipo_algo ==4:
        return quk.sort(data_structs, cmpMapTaxAnio)
    
    if tipo_algo ==5:
        return merg.sort(data_structs, cmpMapTaxAnio)
