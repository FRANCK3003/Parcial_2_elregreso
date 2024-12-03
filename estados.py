import pygame

def escalar_imagenes_fondo (direc_imagen:str,tamanio:tuple):
    """escala la imagen sugun el tamaño dado 

    Args:
        direc_imagen (str): directorio de la imagen
        tamanio (tuple): tapaño a escalar

    Returns:
        superficie 
    """    
    imagen = pygame.image.load(direc_imagen)
    imagen = pygame.transform.scale(imagen,(tamanio))
    return imagen

def banderas(casillas:list):
    for boton in casillas:
        if boton['boton_rec'].collidepoint(pygame.mouse.get_pos()):
            print(boton)
            if boton['clicado'] == False:
                if boton['marcado'] == False:
                    boton['marcado'] = True
                else:
                    boton['marcado'] = False

def boton_clicado(juego,music_stop,cont_puntos,flag1,flag2)->tuple:
    for boton in juego:
        if boton['boton_rec'].collidepoint(pygame.mouse.get_pos()):
            if boton['clicado'] == False:
                if boton['marcado'] == False: # si no fue clicado
                    boton['evento'] = True  # Marcado como clik
                    if boton['texto'] == "-1":
                        music_stop.stop()
                        flag1 = True
                        flag2 = False
                    else:
                        cont_puntos += 1
                        boton['clicado'] = True
    return flag1,flag2,cont_puntos
