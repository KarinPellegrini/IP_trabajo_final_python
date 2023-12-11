import pygame
import random
from pygame.locals import *
from configuracion import *




def dameLetraApretada(key):
    if key == K_a:
        return("a")
    elif key == K_b:
        return("b")
    elif key == K_c:
        return("c")
    elif key == K_d:
        return("d")
    elif key == K_e:
        return("e")
    elif key == K_f:
        return("f")
    elif key == K_g:
        return("g")
    elif key == K_h:
        return("h")
    elif key == K_i:
        return("i")
    elif key == K_j:
        return("j")
    elif key == K_k:
        return("k")
    elif key == K_l:
        return("l")
    elif key == K_m:
        return("m")
    elif key == K_n:
        return("n")
    elif key == K_o:
        return("o")
    elif key == K_p:
        return("p")
    elif key == K_q:
        return("q")
    elif key == K_r:
        return("r")
    elif key == K_s:
        return("s")
    elif key == K_t:
        return("t")
    elif key == K_u:
        return("u")
    elif key == K_v:
        return("v")
    elif key == K_w:
        return("w")
    elif key == K_x:
        return("x")
    elif key == K_y:
        return("y")
    elif key == K_z:
        return("z")
    elif key == K_SPACE:
       return(" ")
    elif key == K_SEMICOLON:
        return("ñ")
    else:
        return("")


def escribirEnPantalla(screen, palabra, posicion, tamano, color):
    defaultFont= pygame.font.Font( pygame.font.get_default_font(), tamano)
    ren = defaultFont.render(palabra, 1, COLOR_TEXTO)
    screen.blit(ren, posicion)

def dibujar(screen, candidata, listaDeSilabas, posiciones, puntos, segundos,):


    defaultFont= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA)

    #Linea del piso
    pygame.draw.line(screen, (255,255,255), (0, ALTO-70) , (ANCHO, ALTO-70), 5)


    ren1 = defaultFont.render(candidata, 1, COLOR_TEXTO)
    ren2 = defaultFont.render("Puntos: " + str(puntos), 1, COLOR_TEXTO)

##    if segundos<30:

    if(segundos<15):
        ren3 = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TIEMPO_FINAL)
    else:
        ren3 = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TEXTO)
##    colores=[(216,191,216),(255,105,180),(0,128,0),(218,165,32),(210,105,30),(255,255,0),(139,0,0)]
##    r=random.choice(colores)
    for i in range(len(listaDeSilabas)):
        colores=[(216,191,216),(255,105,180),(0,128,0),(218,165,32),(210,105,30),(255,255,0),(139,0,0)]
        r=random.choice(colores)
        screen.blit(defaultFont.render(listaDeSilabas[i], 1, r), posiciones[i])

    screen.blit(ren1, (190, 570))
    screen.blit(ren2, (680, 10))
    screen.blit(ren3, (10, 10))