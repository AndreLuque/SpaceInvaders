#-----------------------------------------------------------------------
# SpaceInvaders.py
# Description:
# Author: Ghost
# Date: 10/12/2020
# Version: 1.0
#-----------------------------------------------------------------------
import pygame
import random
import time
from typing import List

NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0 )
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)
AMARILLO = (255,255,0)
GRIS_OSCURO = (175,175,175)
GRIS_CLARO = (150,150,150)
AZUL_CLARO = (0, 255, 255)
NARANJA = (255, 180, 0)
 
def naveEspacial(pantalla, posicionNave_x:int, posicionNave_y:int) -> None:
    #Base principal de la naveEspacial
    pygame.draw.rect(pantalla, BLANCO, (posicionNave_x, posicionNave_y, 30, 15))
    #Seccion azul base principal de la naveEspacial
    pygame.draw.rect(pantalla, AZUL, (posicionNave_x, posicionNave_y + 15, 30, 3))
    #Base disparadores mas externos
    pygame.draw.rect(pantalla, BLANCO, (posicionNave_x - 5, posicionNave_y - 8, 5, 30))
    pygame.draw.rect(pantalla, BLANCO, (posicionNave_x + 30, posicionNave_y - 8, 5, 30))
    #Seccion roja disparadores mas externos
    pygame.draw.rect(pantalla, ROJO, (posicionNave_x - 5, posicionNave_y - 12, 5, 4))
    pygame.draw.rect(pantalla, ROJO, (posicionNave_x + 30, posicionNave_y - 12, 5, 4))
    #Primer rectangulo encima de la base principal de la naveEspacial
    pygame.draw.rect(pantalla, BLANCO, (posicionNave_x + 7, posicionNave_y - 8, 16, 8))
    #Base disparadores intermedios
    pygame.draw.rect(pantalla, BLANCO, (posicionNave_x + 4, posicionNave_y - 18, 3, 18))
    pygame.draw.rect(pantalla, BLANCO, (posicionNave_x + 23, posicionNave_y - 18, 3, 18))
    #Seccion roja disparadores intermedios
    pygame.draw.rect(pantalla, ROJO, (posicionNave_x + 4, posicionNave_y - 22, 3, 4))
    pygame.draw.rect(pantalla, ROJO, (posicionNave_x + 23, posicionNave_y - 22, 3, 4))
    #Segundo rectangulo encima de la base principal de la naveEspacial
    pygame.draw.rect(pantalla, BLANCO, (posicionNave_x + 11, posicionNave_y - 17, 8, 9))
    #Base disparador mas interno
    pygame.draw.rect(pantalla, BLANCO, (posicionNave_x + 13, posicionNave_y - 25, 4, 8))
    #Seccion roja disparador mas interno
    pygame.draw.rect(pantalla, ROJO, (posicionNave_x + 13, posicionNave_y - 28, 4, 3))
    
def aliens(pantalla, posicionAlien:List[int], colorAliens:tuple) -> None:
    #Cabeza alien
    pygame.draw.rect(pantalla, colorAliens, (posicionAlien[0], posicionAlien[1], 18, 16))
    #Ojos Alien
    pygame.draw.rect(pantalla, NEGRO, (posicionAlien[0] + 3, posicionAlien[1] + 8, 3, 3))
    pygame.draw.rect(pantalla, NEGRO, (posicionAlien[0] + 12, posicionAlien[1] + 8, 3, 3))
    #Primera parte piernas alien
    pygame.draw.rect(pantalla, colorAliens, (posicionAlien[0] + 3, posicionAlien[1] + 16, 3, 8))
    pygame.draw.rect(pantalla, colorAliens, (posicionAlien[0] + 12, posicionAlien[1] + 16, 3, 8))
    #Segunda parte piernas alien
    pygame.draw.rect(pantalla, colorAliens, (posicionAlien[0], posicionAlien[1] + 21, 3, 3))
    pygame.draw.rect(pantalla, colorAliens, (posicionAlien[0] + 15, posicionAlien[1] + 21, 3, 3))
    #Primera parte brazos alien
    pygame.draw.rect(pantalla, colorAliens, (posicionAlien[0] - 6, posicionAlien[1] + 8, 6, 3))
    pygame.draw.rect(pantalla, colorAliens, (posicionAlien[0] + 18, posicionAlien[1] + 8, 6, 3))
    #Segunda parte brazos alien
    pygame.draw.rect(pantalla, colorAliens, (posicionAlien[0] - 6, posicionAlien[1] + 11, 3, 3))
    pygame.draw.rect(pantalla, colorAliens, (posicionAlien[0] + 21, posicionAlien[1] + 11, 3, 3))
    #Antennas
    pygame.draw.rect(pantalla, colorAliens, (posicionAlien[0] + 3, posicionAlien[1] - 4, 3, 4))
    pygame.draw.rect(pantalla, colorAliens, (posicionAlien[0] + 12, posicionAlien[1] - 4, 3, 4))

def disparos(pantalla, listaDisparos:List[int]) -> None:
    #Dibujar cada disparo    
    for i in range(len(listaDisparos)):
        pygame.draw.rect(pantalla, VERDE, listaDisparos[i])
 
def corazon(pantalla, vidas:int, posicionCorazon = 30) -> None:
    #Dibujamos un corazon para cada vida que tenga
    for i in range(vidas):
        #Base 1
        pygame.draw.rect(pantalla, ROJO, (posicionCorazon, 30, 30, 10))
        #Base 2
        pygame.draw.rect(pantalla, ROJO, (posicionCorazon + 5, 40, 20, 8))
        #Base 3
        pygame.draw.rect(pantalla, ROJO, (posicionCorazon + 8, 48, 14, 6))
        #Base 4
        pygame.draw.rect(pantalla, ROJO, (posicionCorazon + 12, 54, 6, 6))
        #Cabezas
        pygame.draw.rect(pantalla, ROJO, (posicionCorazon + 3, 24, 8, 6))
        pygame.draw.rect(pantalla, ROJO, (posicionCorazon + 19, 24, 8, 6))
        posicionCorazon += 50
def estrellas(pantalla, listaEstrellas:List[int], countEstrellas:int) -> List[int] and int:
    for i in range(len(listaEstrellas)):
        pygame.draw.rect(pantalla, GRIS_OSCURO, (listaEstrellas[i][0], listaEstrellas[i][1], 1, 3))
        if countEstrellas % 5 == 0:
            listaEstrellas[i][1] += 1
        if listaEstrellas[i][1] > 500:
            y = random.randrange(-30, 0)
            listaEstrellas[i][1] = y
            x = random.randrange(0, 500)
            listaEstrellas[i][0] = x   
    countEstrellas += 1        
    return listaEstrellas, countEstrellas
    
def generarAlien(listaAliens:List[int], y1:int, y2:int) -> List[int]:
    posicionAlien_x = random.randrange(476)
    posicionAlien_y = random.randrange(-100,-50)
    listaAliens += [[posicionAlien_x, posicionAlien_y]]
    return listaAliens
                   
def imagendeFondo(pantalla) -> None:
    #Poner imagen de fondo    
    imagen_defondo = pygame.image.load("galaxy.jpg")    
    pantalla.blit(imagen_defondo, [0, 0])
    #Definimos el font de nuestros textos
    fuente = pygame.font.Font('ARCADE_N.ttf', 50)
    #Dos capas del mensaje Space
    texto = fuente.render('Space', True, BLANCO)
    pantalla.blit(texto, [125, 95])
    texto = fuente.render('Space', True, VERDE)
    pantalla.blit(texto, [130, 100])    
    #Dos capas del mensaje Invaders
    texto = fuente.render('Invaders', True, BLANCO)
    pantalla.blit(texto, [55, 155])
    texto = fuente.render('Invaders', True, VERDE)
    pantalla.blit(texto, [60, 160])      
                   
def botonInicio(pantalla, countColor:int) -> None:
    #Ir alternando los diferentes tonos de gris
    countColor += 1
    if (countColor // 50) % 2 == 0 :
        colorActual = GRIS_CLARO
    else:
        colorActual = GRIS_OSCURO
    pygame.draw.rect(pantalla, colorActual , (85, 250, 350, 50))   
    #Decirle al usuario que teclee return para empezar
    fuente = pygame.font.Font('ARCADE_N.ttf', 12)
    texto = fuente.render("Press 'enter' to start", True, BLANCO)
    pantalla.blit(texto, [125, 265])  
    #Copyright
    fuente = pygame.font.Font('ARCADE_N.ttf', 5)
    texto = fuente.render('Copyright © 2020 by André Queiroz. All rights reserved.', True, BLANCO)
    pantalla.blit(texto, [120, 305]) 
    #retornar el valor actual de count para determinar el color
    return countColor    
    
def botonPlayAgain(pantalla, countColor:int) -> None:
    #Ir alternando los diferentes tonos de gris
    countColor += 1
    if (countColor // 50) % 2 == 0 :
        colorActual = GRIS_CLARO
    else:
        colorActual = GRIS_OSCURO
    pygame.draw.rect(pantalla, colorActual , (85, 260, 350, 50))   
    #Decirle al usuario que teclee return para empezar
    fuente = pygame.font.Font('ARCADE_N.ttf', 12)
    texto = fuente.render("Press 'enter' to play again", True, BLANCO)
    pantalla.blit(texto, [100, 275])  
    #retornar el valor actual de count para determinar el color
    return countColor    
    
def posicionNave(posicionNave_x:int, posicionNave_y:int, velocidadNave_x:int, velocidadNave_y) -> int:
    if posicionNave_x - 5 + velocidadNave_x < 0:
        posicionNave_x = 5
    elif posicionNave_x + 35 + velocidadNave_y > 500:
        posicionNave_x = 464
    else:
        posicionNave_x += velocidadNave_x
    if posicionNave_y - 28 + velocidadNave_y < 0:
        posicionNave_y = 28
    elif posicionNave_y  + 22 + velocidadNave_y > 500:
        posicionNave_y = 478
    else:
        posicionNave_y += velocidadNave_y 
    return posicionNave_x, posicionNave_y
    
def posicionDisparos(listaDisparos:List[int], movDisparo_y, i:int) -> List[int]:
    for j in range(len(listaDisparos[0])):
                if listaDisparos[i][j][1] < -5:
                    listaDisparos[i][j] = [1000, 1000, 1, 1]
                else:    
                    listaDisparos[i][j][1] += movDisparo_y
    return listaDisparos
    
def nuevoDisparo(posicionNave_x, posicionNave_y, listaDisparos1, listaDisparos2, listaDisparos3) -> List[int]:
    # Guardar la info de las posiciones de los disparos del primer disparador
    listaDisparo = [posicionNave_x + 4, posicionNave_y - 32, 1, 8]
    listaDisparos1 += [listaDisparo]
    # Guardar la info de las posiciones de los disparos del segundo disparador
    listaDisparo = [posicionNave_x + 23, posicionNave_y - 32, 1, 8]
    listaDisparos2 += [listaDisparo]
    # Guardar la info de las posiciones de los disparos del tercer disparador
    listaDisparo = [posicionNave_x + 13, posicionNave_y - 38, 1, 8]
    listaDisparos3 += [listaDisparo]  
    return listaDisparos1, listaDisparos2, listaDisparos3
    
def reproducirSonido(sonido:str) -> None:
    #Reproduce el sonido elegido
    reproducir = pygame.mixer.Sound(sonido)
    reproducir.play()
    return reproducir

def DibujVidaExtra(pantalla, posicionVidaExtra) -> None:    
    #Dibujamos la vida extra donde el alien ha muerto
    #Base 1
    pygame.draw.rect(pantalla, ROJO, (posicionVidaExtra[0], posicionVidaExtra[1], 9, 3))
    #Base 2
    pygame.draw.rect(pantalla, ROJO, (posicionVidaExtra[0] + 1, posicionVidaExtra[1] + 3, 7, 3))
    #Base 3
    pygame.draw.rect(pantalla, ROJO, (posicionVidaExtra[0] + 3, posicionVidaExtra[1] + 6, 4, 2))
    #Base 4
    pygame.draw.rect(pantalla, ROJO, (posicionVidaExtra[0] + 4, posicionVidaExtra[1] + 8, 2, 2))
    #Cabezas
    pygame.draw.rect(pantalla, ROJO, (posicionVidaExtra[0] + 1, posicionVidaExtra[1] - 1, 2, 2))
    pygame.draw.rect(pantalla, ROJO, (posicionVidaExtra[0] + 6, posicionVidaExtra[1] - 1, 2, 2))
   
def choqueAliensDisparos(listaAliens, listaDisparos:List[int], puntos:int, vidaExtra:bool, posicionVidaExtra = List[int]) -> List[int] and List[int] and int and bool:
    #Si la posicion del disparo coincide con la posicion de algun alien, desaparece ese alien y ese disparo    
    for i in listaAliens:
        j = 0
        while j < len(listaDisparos):
            if i[0] - 6 <= listaDisparos[j][0] <= i[0] + 24 and listaDisparos[j][1] <= i[1] + 24 and listaDisparos[j][1] + 8 >= i[1] - 4:
                #Hay una posibilidad de 3,33% que despues de matar un alien suelte una vida extra
                r = random.randrange(1,31)
                if r == 30 and vidaExtra == False:
                    vidaExtra = True
                    posicionVidaExtra = i
                listaAliens.remove(i)
                listaAliens = generarAlien(listaAliens, -100, -50)
                listaDisparos[j] = [1000, 1000, 1, 1]
                puntos += 50  #El usuario gana 50 puntos cada vez que mata a un alien 
                j = 3
            j += 1    
    return listaAliens, listaDisparos, puntos, vidaExtra, posicionVidaExtra

def choqueAliensNave(pantalla, listaAliens:List[int], posicionNave_x:int, posicionNave_y:int, vidas:int, explosion = False) -> List[int] and int and bool:
    for i in listaAliens:
        if (posicionNave_x + 35 >= i[0] - 6 and posicionNave_x  - 5 <= i[0] + 24 and posicionNave_y - 31 <= i[1] + 24 and posicionNave_y + 22 >= i[1] - 4) or i[1] - 4 >= 500:
            vidas += -1
            explosion = True
            #Sonido explosion
            reproducirSonido('bazooka+3.wav')
            #Explosion cuando choca    
            pygame.draw.circle(pantalla, NARANJA, [i[0], i[1]], 20)
            listaAliens.remove(i)
            listaAliens = generarAlien(listaAliens, -100, -50)
    return listaAliens, vidas, explosion

def choqueNaveVidaExtra(posicionNave_x:int, posicionNave_y:int, posicionVidaExtra:List[int], vidas:int, vidaExtra = True) -> int and bool:
    if posicionNave_x + 35 >= posicionVidaExtra[0] - 5 and posicionNave_x  - 5 <= posicionVidaExtra[0] + 15 and posicionNave_y - 31 <= posicionVidaExtra[1] + 15 and posicionNave_y + 22 >= posicionVidaExtra[1] - 5:
        vidas += 1
        vidaExtra = False
        reproducirSonido('smb_powerup.wav')
    return vidas, vidaExtra
    
def colorGameOver(pantalla, color_x:int, color_y:int, cambioColor_x:int, cambioColor_y:int, tamañoCirculo:int, crecCirculo = 5, hecho = False) -> int and bool:
    color_x += cambioColor_x
    color_y += cambioColor_y
    tamañoCirculo += crecCirculo
    color = (98 + color_x, 12 + color_y, 255)
    pygame.draw.circle(pantalla, color, [250, 250], tamañoCirculo)
    if  250 < 98 + color_x or 98 + color_x < 5:
        cambioColor_x = cambioColor_x * -1
    elif  250 < 12 + color_y or 12 + color_y < 5:
        cambioColor_y = cambioColor_y * -1   
    if tamañoCirculo == 2000:
        hecho = True 
    return color_x, color_y, cambioColor_x, cambioColor_y, tamañoCirculo, hecho   
    
def pantallaDificultad(pantalla, pos:List[int], boton1 = BLANCO, boton2 = BLANCO, boton3 = BLANCO) -> None:
    if  100 <= pos[0] <= 425 and 100 <= pos[1] <= 175: 
        boton1 = GRIS_OSCURO
    elif 100 <= pos[0] <= 425 and 200 <= pos[1] <= 275: 
        boton2 = GRIS_OSCURO
    elif 100 <= pos[0] <= 425 and 300 <= pos[1] <= 375:
        boton3 = GRIS_OSCURO
    pygame.draw.rect(pantalla, boton1, (80, 100, 325, 75))
    pygame.draw.rect(pantalla, boton2, (80, 200, 325, 75))
    pygame.draw.rect(pantalla, boton3, (80, 300, 325, 75))
    fuente = pygame.font.Font('ARCADE_N.ttf', 16)
    texto = fuente.render("Choose a level of Difficulty:", True, BLANCO)
    pantalla.blit(texto, [25, 50])
    fuente = pygame.font.Font('ARCADE_N.ttf', 20)
    texto = fuente.render("Easy   :)", True, NEGRO)
    pantalla.blit(texto, [180, 120]) 
    texto = fuente.render("Medium   :|", True, NEGRO)
    pantalla.blit(texto, [180, 220]) 
    texto = fuente.render("Hard    :(", True, NEGRO)
    pantalla.blit(texto, [180, 320]) 
   
def main (): 
    #Booleano para determinar si el programa del juego entero se ejectua otra vez
    playAgain = True
    # Inicio
    pygame.init()
    #El usuario jugara tantas veces como quiera si le da al boton play again, establecemos esta variable como True
    while playAgain == True:
        playAgain = False
        # Establecemos el largo y alto de la pantalla [largo,alto]
        dimensiones = [500, 500]
        pantalla = pygame.display.set_mode(dimensiones)#, pygame.FULLSCREEN# 
        pygame.display.set_caption("ARCADE")
        #DECLARACIÓN DE VARIABLES  
        #Iteramos hasta que el usuario pulsa el botón de salir.
        salir = False
        #Booleana para determinar cuando el usuario cumpla los requisitos para ir a la siguente pantalla
        hecho = False
        #Booleano para determinar cuando ha habido una explosion, usuario pierde una vida
        explosion = False
        # Velocidad, en píxeles, por fotograma
        velocidadNave_x= 0
        velocidadNave_y = 0 
        # Posición actual
        posicionNave_x = 235
        posicionNave_y = 400
        #Determina si el usuario esta disparando no
        shoot = False
        #Cuantos disparos actuales hay
        numeroDisparos = 0
        #La velocidad y movimiento de los disparos
        movDisparo_y = -5
        #Listas para la posicion actual de cada disparo anterior (Hay tres disparadores)
        listaDisparos1 = []
        listaDisparos2 = []
        listaDisparos3 = []
        #Velocidad a la que se mueve los aliens
        movAliens = 1
        #Vidas iniciales del usuario
        vidas = 3
        #Los puntos iniciales, acumulara mas matando a aliens
        puntos = 0
        #El color inicial del circulo en la pantalla de game over
        color_x = 0
        color_y = 0
        #La velocidad de cambio del color
        cambioColor_x = 5
        cambioColor_y = 5
        #tamaño inicial del circulo
        tamañoCirculo = 500
        #Variable para determinar cuando cambia de color
        countColor = 0
        #Booleano para ver si ha matado un alien que ha soltado una vidaExtra
        vidaExtra = False
        #Lista que guarda la posicion del alien muerto que ha dejado una vida extra
        posicionVidaExtra = []
        #El color de los aliens en funcion de la dificultad elegido
        colorAliens = NEGRO
        numeroAliens = 0
        #Creamos las estrellas que haran de fondo en nuestro juego 
        listaEstrellas = []    
        for i in range(100):
            x = random.randrange(0, 500)
            y = random.randrange(0, 500)
            listaEstrellas += [[x, y]]
        #Variable para que las estrellas avancen cada 3 fotogramas
        countEstrellas = 1
        # Usamos esto para gestionar cuán rápido se actualiza la pantalla.
        reloj = pygame.time.Clock()
        #PANTALLA DE INTRODUCCIÓN
        sonido = reproducirSonido('party.wav') #Poner sonido intro
        while not hecho and not salir: 
            pos = pygame.mouse.get_pos()
            for evento in pygame.event.get(): 
                if evento.type == pygame.QUIT: # Si el usuario hace click sobre cerrar, saldrá del programa
                    salir = True               
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q: #Si el usuario presiona q, saldrá del programa
                        salir = True
                    #Si el usuario presiona el enter , se empezara el juego    
                    elif evento.key == pygame.K_RETURN:
                        hecho = True
                elif evento.type == pygame.MOUSEBUTTONDOWN and  85 <= pos[0] <= 435 and 250 <= pos[1] <= 300:
                        hecho = True
            pantalla.fill(NEGRO) 
            imagendeFondo(pantalla) #Ponemos una imagen de fondo    
            countColor = botonInicio(pantalla, countColor) #Dibujamos el boton de inicio
            # Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
            pygame.display.flip()
            # Limitamos a 60 fotogramas por segundo
            reloj.tick(60)     
        #PANTALLA DE ELECCIÓN DE DIFICULTAD
        hecho = False
        while not hecho and not salir:
            pos = pygame.mouse.get_pos()
            for evento in pygame.event.get(): 
                if evento.type == pygame.QUIT: # Si el usuario hace click sobre cerrar, saldrá del programa
                    salir = True               
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q: #Si el usuario presiona q, saldrá del programa
                        salir = True
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                        hecho = True
                        reproducirSonido('smb_pipe.wav')
                        time.sleep(1.8)
                        if  100 <= pos[0] <= 425 and 100 <= pos[1] <= 175: 
                            numeroAliens = 6
                            colorAliens = AZUL_CLARO
                        elif 100 <= pos[0] <= 425 and 200 <= pos[1] <= 275: 
                            numeroAliens = 8
                            colorAliens = AMARILLO 
                        elif 100 <= pos[0] <= 425 and 300 <= pos[1] <= 375:
                            numeroAliens = 10
                            colorAliens = VIOLETA    
            pantalla.fill(NEGRO)
            pantallaDificultad(pantalla, pos)
            # Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
            pygame.display.flip()
            # Limitamos a 60 fotogramas por segundo
            reloj.tick(60)
        #Creamos los aliens segund la dificultad elegida
        listaAliens = []
        for i in range(numeroAliens):
            generarAlien(listaAliens, 0, 100)        
        #PANTALLA JUEGO
        hecho = False #reiniciamos hecho como false, si se cumple los requisitos, volverá a true y se saldrá de esta pantalla
        while vidas > 0 and not hecho and not salir: 
            # Ocultamos el cursor del ratón.
            pygame.mouse.set_visible(0)
            for evento in pygame.event.get():  
                if evento.type == pygame.QUIT: # Si el usuario hace click sobre cerrar, se saldrá del programa
                    salir = True                
                elif evento.type == pygame.KEYDOWN:
                    # Mira si ha sido una de las flechas. Si es así
                    # ajusta la velocidad.
                    if evento.key == pygame.K_q:
                        salir = True
                    elif evento.key == pygame.K_LEFT:
                        velocidadNave_x = -10
                    elif evento.key == pygame.K_RIGHT:
                        velocidadNave_x = 10
                    elif evento.key == pygame.K_UP:
                        velocidadNave_y = -5
                    elif evento.key == pygame.K_DOWN:
                        velocidadNave_y = 5
                    elif evento.key == pygame.K_SPACE:
                        shoot = True #Demuestra que ha habido un disparo
                    else:
                        None      
                # El usuario deja de presionar la tecla
                elif evento.type == pygame.KEYUP:
                    # Si es una de las flechas, resetea el vector a cero.
                    if evento.key == pygame.K_LEFT:
                        velocidadNave_x = 0
                    elif evento.key == pygame.K_RIGHT:
                        velocidadNave_x = 0
                    elif evento.key == pygame.K_UP:
                        velocidadNave_y = 0
                    elif evento.key == pygame.K_DOWN:
                        velocidadNave_y = 0
                    elif evento.key == pygame.K_SPACE:
                        shoot = False
            pantalla.fill(NEGRO)#Dibujamos la pantalla de negro   
            #Dibujamos ante todo las estrellas que seran el fondo de nuestro programa
            listaEstrellas, countEstrellas = estrellas(pantalla, listaEstrellas, countEstrellas)
            # Desplaza al objeto según el vector velocidad.
            posicionNave_x, posicionNave_y =  posicionNave(posicionNave_x, posicionNave_y, velocidadNave_x, velocidadNave_y)
            #Si ha habido un disparo lo añadiremos a la lista
            if shoot == True:
                #sonido disparo
                reproducirSonido('laser5.ogg')
                listaDisparos1, listaDisparos2, listaDisparos3 = nuevoDisparo(posicionNave_x, posicionNave_y, listaDisparos1, listaDisparos2, listaDisparos3)
            shoot = False  #Reiniciamos el booleano shoot
            #Cuando un disparo y un alien coinciden en su posicion, desparecen. Llamo a la funcion que comprueba esto tres veces, una para cada disparo
            listaDisparos = [listaDisparos1, listaDisparos2, listaDisparos3]
            for i in range(3):
                listaAliens, listaDisparos[i], puntos, vidaExtra, posicionVidaExtra = choqueAliensDisparos(listaAliens, listaDisparos[i], puntos, vidaExtra, posicionVidaExtra)
            for i in range(3):    
                #Actualizamos las posiciones de los disparos    
                listaDisparos = posicionDisparos(listaDisparos, movDisparo_y, i)   
            #Vemos si la nave choca con algun alien o alguno de estos supera la posicion 500, dibujaremos una explosion en caso afirmativo
            listaAliens, vidas, explosion = choqueAliensNave(pantalla, listaAliens, posicionNave_x, posicionNave_y, vidas)
            #Actualizamos la posicion de los Aliens
            for i in listaAliens:
                i[1] += movAliens
            #Vemos si la posicion de la nave coincide con la vida extra
            if vidaExtra == True:
                vidas, vidaExtra = choqueNaveVidaExtra(posicionNave_x, posicionNave_y, posicionVidaExtra, vidas)    
            #Dibujar la vida extra si la hay, y no la ha cogido todavia
            if vidaExtra == True:
                DibujVidaExtra(pantalla, posicionVidaExtra)
            #Dibujamos la nave espacial         
            naveEspacial(pantalla, posicionNave_x, posicionNave_y)
            #Dibujamos los disparos
            for i in range(3):
                disparos(pantalla, listaDisparos[i])
            #Dibujamos los Aliens
            for i in listaAliens:
                aliens(pantalla, i, colorAliens) 
            #El usuario tendrá un máximo de 6 vidas
            if vidas > 6:
                vidas = 6
            #Demostracion gráfica de las vidas que tiene el usuario
            corazon(pantalla, vidas) 
            #Representando graficamente los puntos que tiene el usuario    
            fuente = pygame.font.Font('ARCADE_N.ttf', 30)
            texto = fuente.render(str(puntos), True, BLANCO)
            pantalla.blit(texto, [375, 30])   
            # Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
            pygame.display.flip()
            #Queremos congelar la pantalla momentaneamente si se ha producido una explosion para que lo vea el usuario
            if explosion == True:
                time.sleep(0.15)   
            #Reproducir nuevo sonido si pierde todas las vidas 
            if vidas == 0:
                sonido.stop() #Paramos el sonido del juego
                #Reproducir sonido de muerte
                reproducirSonido('smb_mariodie.wav')
                time.sleep(3.5) #Queremos parar el juego hasta que se finaliza el sonido
            # Limitamos a 60 fotogramas por segundo
            reloj.tick(60)
            
        #PANTALLA GAME OVER
        hecho = False #Reinicializamos el booleano    
        while not hecho and not salir and not playAgain: 
            # Dejamos de ocultar el cursor del ratón.
            pygame.mouse.set_visible(1)
            pos = pygame.mouse.get_pos()
            for evento in pygame.event.get():  
                if evento.type == pygame.QUIT: # Si el usuario hace click sobre cerrar, saldrá del programa
                    salir = True               
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        salir = True
                    elif evento.key == pygame.K_RETURN:
                        playAgain = True
                    else:
                        None
                elif evento.type == pygame.MOUSEBUTTONDOWN and  85 <= pos[0] <= 435 and 260 <= pos[1] <= 310:
                        playAgain = True        
            pantalla.fill(NEGRO)  #Ponemos la pantalla en negro
            #Círculo cambiando constantemente de tamaño y colors
            color_x, color_y, cambioColor_x, cambioColor_y, tamañoCirculo, hecho = colorGameOver(pantalla, color_x, color_y, cambioColor_x, cambioColor_y, tamañoCirculo)
            #Mostrar el mensaje Game Over    
            fuente = pygame.font.Font('ARCADE_N.ttf', 50)
            texto = fuente.render('Game Over', True, BLANCO)
            pantalla.blit(texto, [30, 200])
            #Vamos alternando los colores del boton de Play Again
            countColor = botonPlayAgain(pantalla, countColor)     
            # Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
            pygame.display.flip()
            # Limitamos a 60 fotogramas por segundo
            reloj.tick(60)
            
                
    pygame.quit()

if __name__ == '__main__': main()