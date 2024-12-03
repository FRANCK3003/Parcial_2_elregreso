import pygame

def escalar_imagenes_fondo (direc_imagen:str,tamanio:tuple):
    """Carga la imagen y la escala segun el tamaño dado 

    Args:
        direc_imagen (str): directorio de la imagen
        tamanio (tuple): tapaño a escalar

    Returns:
        superficie: imagen escalada
    """    
    imagen = pygame.image.load(direc_imagen)
    imagen = pygame.transform.scale(imagen,(tamanio))
    return imagen

def banderas(casillas:list):
    """
    Alterna el estado de marcado (bandera) en las casillas del tablero de juego al hacer clic derecho.
    Args:
        casillas (list): Lista de diccionarios
    """
    for boton in casillas:
        if boton['boton_rec'].collidepoint(pygame.mouse.get_pos()):
            if boton['clicado'] == False:
                if boton['marcado'] == False:
                    boton['marcado'] = True
                else:
                    boton['marcado'] = False

def boton_clicado(juego:list,musica:pygame.mixer.Sound,cont_puntos:int,flag_juego,flag2)->tuple:
    """Procesa el clic de una casilla del tablero, actualizando su estado y maneja estados del juego.
        determina si hizo clik en bomba y si no es marca evento en true y suma el punto correspondiente
    Args:
        juego (list): lista de diccionarios
        musica (pygame.mixer.Sound): Musica (mixer.sound)
        cont_puntos (int): Contador de puntos 
        flag_juego (_type_): bandera 1
        flag2 (_type_): Bandera 2

    Returns:
        tuple: tupla con los valores actualizados de flag_juego,flag2,cont_puntos
    """
    for boton in juego:
        if boton['boton_rec'].collidepoint(pygame.mouse.get_pos()):
            if boton['clicado'] == False:
                if boton['marcado'] == False: # si no fue clicado
                    boton['evento'] = True  # Marcado como clik
                    if boton['texto'] == "-1":
                        musica.stop()
                        flag_juego = True
                        flag2 = False
                    else:
                        cont_puntos += 1
                        boton['clicado'] = True
    return flag_juego,flag2,cont_puntos
