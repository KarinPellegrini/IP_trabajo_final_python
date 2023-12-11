#! /usr/bin/env python
import os, random, sys, math

import pygame
from pygame.locals import *

from configuracion import *
from extras import *
from funcionesSeparador import *
from funcionesVACIAS import *

#Funcion principal
def main():
        #Centrar la ventana y despues inicializar pygame
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load('Benny Hill Theme.mp3') ##carga la musica de fondo
        pygame.mixer.music.play()






        #Preparar la ventana
        pygame.display.set_caption("En Si-La-Bas...")
        final = pygame.image.load("fondo.jpg")##carga la imagen para el fondo del game over y top10
        fondo = pygame.image.load("fondito.jpg")##carga la imagen para el juego
        inicio = pygame.image.load("inicio2.jpg")
        fondo=pygame.transform.scale(fondo, (ANCHO, ALTO))
        inicio=pygame.transform.scale(inicio, (ANCHO, ALTO))
        screen = pygame.display.set_mode((ANCHO, ALTO))



        #tiempo total del juego
        gameClock = pygame.time.Clock()
        rapido=1
        totaltime = 0
        segundos=TIEMPO_MAX
        fps = FPS_inicial


        puntos = 0
        candidata = ""
        silabasEnPantalla = []
        posiciones = []
        listaDeSilabas=[]
        lemario=[]

        archivo= open("silabas.txt","r")
        lectura(archivo, listaDeSilabas)

        archivo2= open("lemario.txt","r")
        lectura(archivo2, lemario)


        dibujar(screen, candidata, silabasEnPantalla, posiciones, puntos,segundos)
        texto_intro = pygame.font.SysFont("console", 30, True)
        texto_intro_2=pygame.font.SysFont("ArialBlack", 52)

        esta_en_intro = True


        while esta_en_intro:
            for evento in pygame.event.get():
                if evento.type == QUIT:
                    pygame.quit()
                    return()





            screen.fill((0,0,0))
            titulo = texto_intro_2.render("En sí - la - bas...",1,(255, 51, 233))
            reglas= texto_intro.render("¡Arma la mayor cantidad de palabras!",1,(128,0,128))
            minuto= texto_intro.render("ATENCIÓN: Tienes un minuto",1,(255, 0, 0))
            instrucciones= texto_intro.render("Presione ENTER para continuar...",1,(0,0,0))

            screen.blit(inicio,(0,0))
            screen.blit(titulo, ((ANCHO//2)-titulo.get_width()//2, 10))
            screen.blit(reglas, ((ANCHO//2)-reglas.get_width()//2, 100))
            screen.blit(minuto, ((ANCHO//2)-minuto.get_width()//2, 150))
            screen.blit(instrucciones, ((ANCHO//2)-instrucciones.get_width()//2, 300))


            tecla= pygame.key.get_pressed()



            if tecla[pygame.K_RETURN]:
                esta_en_intro = False



            pygame.display.update()

        aux=1
        tiempo=pygame.time.get_ticks()/1000
        if aux==tiempo:
            aux+=1
        print (tiempo)



##        segundos=segundos+tiempo


        while (segundos) > fps/1000:
        # 1 frame cada 1/fps segundos


            gameClock.tick(fps*rapido)
            if segundos<15:##a los 30 segundos aumenta la velocidad en la que descienden las silabas
                  rapido=3


            totaltime += gameClock.get_time()

            if True:
            	fps = 3

            #Buscar la tecla apretada del modulo de eventos de pygame
            for e in pygame.event.get():

                #QUIT es apretar la X en la ventana
                if e.type == QUIT:
                    pygame.quit()
                    return()

                #Ver si fue apretada alguna tecla
                if e.type == KEYDOWN:
                    letra = dameLetraApretada(e.key)
                    candidata += letra
                    if e.key==241:
                        candidata+="ñ"
                    if e.key == K_BACKSPACE:
                        candidata = candidata[0:len(candidata)-1]
                    if e.key == K_RETURN:
                        puntuacion = procesar(candidata, silabasEnPantalla, posiciones, lemario)
                        efectoPuntuacion(puntuacion)
                        puntos += puntuacion
                        candidata = ""


            segundos = (TIEMPO_MAX +tiempo) - pygame.time.get_ticks()/1000


            #Limpiar pantalla anterior
##            screen.fill(COLOR_FONDO)
            screen.blit(fondo,(0,0))


            #Dibujar de nuevo todo
            dibujar(screen, candidata, silabasEnPantalla, posiciones, puntos, segundos)

            pygame.display.flip()


            actualizar(silabasEnPantalla, posiciones, listaDeSilabas)
        # aqui se imprime el Game Oveer y se espera el nombre del jugador
        # una vez cargado el nombre se muestra el top ten

        guardado=False
        nombre=""
        listaPuntuaciones = []
        while 1:
            #Esperar el QUIT del usuario

            for e in pygame.event.get():
                if e.type == QUIT:
                    pygame.quit()
                    return
                #Ver si fue apretada alguna tecla
                if guardado == False and e.type == KEYDOWN:
                    letra = dameLetraApretada(e.key)
                    nombre += letra
                    if e.key == K_BACKSPACE:
                        nombre = nombre[0:len(candidata)-1]
                    if e.key == K_RETURN:
                        guardarPuntaje(puntos,nombre)
                        guardado=True
            screen.blit(final,(0,0))
            #Dibujar de nuevo todo
            pygame.mixer.music.stop()
            sound=pygame.mixer.Sound("oh no01.ogg")
##            sound.play()
            escribirEnPantalla(screen, "GAME OVER", Punto(260,100), 50, COLOR_TIEMPO_FINAL)
            if guardado:
                if len(listaPuntuaciones) == 0:
                    listaPuntuaciones = topTen()
                dY=0
                for (topPuntos,topNombre) in listaPuntuaciones:
                    escribirEnPantalla(screen, str(topPuntos)+"    ......", Punto(200,200+dY), 30, COLOR_LETRAS)
                    escribirEnPantalla(screen, topNombre, Punto(350,200+dY), 30, COLOR_LETRAS)
                    dY = dY+35
            else:
                escribirEnPantalla(screen, str(puntos)+"    ......", Punto(200,200), 30, COLOR_LETRAS)
                escribirEnPantalla(screen, nombre, Punto(350,200), 30, COLOR_LETRAS)
            pygame.display.flip()


        while 1:
            #Esperar el QUIT del usuario
            for e in pygame.event.get():
                if e.type == QUIT:
                    pygame.quit()
                    return

#Programa Principal ejecuta Main
if __name__ == "__main__":
    main()
