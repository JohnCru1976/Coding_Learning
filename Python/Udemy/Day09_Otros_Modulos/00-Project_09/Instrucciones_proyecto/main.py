'''Ejercicio de formación para manejo de archivos y string literals'''
import os
import re
from pathlib import Path
import datetime
import time
import math

PATRON = r'N\w{3}-\d{5}'

def change_working_directory():
    '''Establece como directorio de trabajo el directorio del archivo'''
    file_diretory = os.path.dirname(__file__)
    os.chdir(file_diretory)
    return file_diretory

def lista_path_files(path, patron):
    '''Devuelve una lista de tuplas con el nombre del archivo y la contraseña'''
    rutas = os.walk(path)
    lista_path = []
    for carpeta, subcarpeta, archivos in rutas:
        if archivos:
            for archivo in archivos:
                ruta = Path(carpeta, archivo)
                # Comprobar el texto del archivo y devolver la tupla
                evaluacion = evaluar_coincidencia(ruta, patron)
                if evaluacion:
                    lista_path.append((archivo, evaluacion))
    return lista_path

def evaluar_coincidencia(ruta_archivo, patron):
    '''Función que devuelve la contraseña en caso de que se produzca coindicencia'''
    # Recorrer las líneas de un archivo
    mi_archivo = open(ruta_archivo,"r")
    evaluacion = ""
    for linea in mi_archivo:
        evaluacion = re.search(patron, linea)
        if evaluacion:
            break
    mi_archivo.close()
    if evaluacion:
        return evaluacion.group()
    return evaluacion

def fecha_actual():
    '''Devuelve un string con la fecha actual en formato dd/mm/yy'''
    fecha_actual = datetime.date.today()
    dia  = fecha_actual.day
    mes  = fecha_actual.month
    anio  = fecha_actual.year
    return f"{str(dia).zfill(2)}/{str(mes).zfill(2)}/{str(anio).zfill(2)}"

def presentacion (listado_coincidencias):
    #Se toma el tiempo de inicio
    tiempo_inicio = time.time()
    print("----------------------------------------------------")
    print("Fecha de búsqueda: " + fecha_actual() + "\n")
    print("ARCHIVO\t\t\tNRO. SERIE")
    print("-------\t\t\t----------")
    # Se imprime el listado de coincidencias
    for tupla in listado_coincidencias:
        if len(tupla[0]) > 13:
            print(str(tupla[0]) +"\t" + str(tupla[1]))
        else:
            print(str(tupla[0]) +"\t\t" + str(tupla[1]))
    print(f"\nNúmeros encontrados: {len(listado_coincidencias)}")
    # Se toma el tiempo final
    tiempo_fin = time.time()
    # Se imprime la duración del proceso
    print(f"Duración de la búsqueda: {math.ceil(tiempo_fin-tiempo_inicio)} segundos")
    print("----------------------------------------------------")


if __name__ == "__main__" :
    tuplas_archivo_coincidencia = lista_path_files(change_working_directory(),PATRON)
    presentacion(tuplas_archivo_coincidencia)
