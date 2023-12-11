from principal import *
from configuracion import *
from funcionesSeparador import *
from extras import *


import random
import math
import pygame




def lectura(archivo, lista):
    arc= archivo.readlines()
    for linea in arc:
        lista.append(linea[:-1])


def actualizar(silabasEnPantalla,posiciones,listaDeSilabas):
    silaba=nuevaSilaba(listaDeSilabas)
    silabasEnPantalla.append(silaba)
    x=random.randrange(10,ANCHO-25)
    y=-16
    pos=[x,y]
    posiciones.append(pos)
    i=0
    while i < (len(posiciones)):
        if posiciones[i][1] < ALTO -90:
            posiciones[i][1]+=16
            i=i+1
        else:
            silabasEnPantalla.pop(i)
            posiciones.pop(i)

def nuevaSilaba(silabas):
    return random.choice(silabas)

def quitar(candidata, silabasEnPantalla, posiciones):
    silabas=dameSilabas(candidata)
    for elem in silabas:
        i = silabasEnPantalla.index(elem) # modificar para que elimine la repetida que está más abajo.
        silabasEnPantalla.pop(i)
        posiciones.pop(i)

def dameSilabas(candidata):
    listaSilabas=[]
    nueva=""
    palabraSeparada=separador(candidata)
    for caracter in palabraSeparada+"-":
        if caracter!="-":
            nueva=nueva+caracter
        else:
            listaSilabas.append(nueva)
            nueva="" #incluir en el reporte
    return listaSilabas


def esValida(candidata, silabasEnPantalla, lemario):
    suma=0
    listaCandidataSilabas=dameSilabas(candidata)
    for i in range(len(listaCandidataSilabas)):
        if listaCandidataSilabas[i] in silabasEnPantalla:
            suma=suma+1

    if suma==len(listaCandidataSilabas) and candidata in lemario:
        return True
    return False

def Puntos(candidata):
    puntos=0
    for letra in candidata.lower():
        if letra== "a" or letra== "e" or letra== "i" or letra== "o" or letra== "u":
            puntos=puntos+1
        elif letra== "k" or letra=="q" or letra=="w" or letra=="x" or letra=="y" or letra=="z" or letra=="ñ":
            puntos=puntos+5
        else:
            puntos=puntos+2
    return puntos

def procesar(candidata, silabasEnPantalla, posiciones, lemario):

    if esValida(candidata, silabasEnPantalla, lemario)==True:
        puntosDePalabra=Puntos(candidata)
        quitar(candidata, silabasEnPantalla, posiciones)
    else:
        puntosDePalabra=0
    return puntosDePalabra


def guardarPuntaje(puntos,nombre):
    with open("topTen.txt","a") as archivo:
        archivo.write(str(puntos)+";"+nombre+"\n")
        archivo.close()

def topTen():
    listaPuntos = []
    topPuntos=[]
    cant = 0
    archivo = open("topTen.txt","r")
    for linea in archivo.readlines():
        listaPuntos.append( tuple( linea.strip().split(';') ) )
        cant = cant + 1

    if cant < 10:
        for i in range(cant,10):
            listaPuntos.append( tuple( [0,"vacio"]) )

    listaPuntos.sort( key=lambda tup: int(tup[0]),reverse=True )

    cant = 0
    for tupla in listaPuntos:
        topPuntos.append(tupla)
        cant = cant + 1
        if cant == 10:
            break

    return topPuntos


def efectoPuntuacion(puntos):
    if puntos > 1:
        sound=pygame.mixer.Sound("Correcto.ogg")
        sound.play()##si no funciona bien quitar esta linea
    elif puntos == 0:
        sound=pygame.mixer.Sound("Error.ogg")
        sound.play()##si no funciona bien quitar esta linea



