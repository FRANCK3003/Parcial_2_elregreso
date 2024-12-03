import pygame
# from botones import escalar_imagenes_fondo
from estados import escalar_imagenes_fondo

# resolucion de pantalla
pygame.init()
PANTALLA_ANCHO = 1280
PANTALLA_LARGO = 720

SIZE_SCREEN = PANTALLA_ANCHO,PANTALLA_LARGO
SCREEN = pygame.display.set_mode(SIZE_SCREEN)

PATH = 'assets'
# fuentes 
FUENTE_1 = pygame.font.Font(f"{PATH}/fuente_texto.otf",25)

FUENTE_2 = pygame.font.SysFont("Arial black",25)
FUENTE_3 = pygame.font.Font(f"{PATH}/fuente_texto.otf",40)
FUENTE_ENCABEZADO = pygame.font.SysFont("Arial black",40)

# imagenes
icon_image = pygame.image.load("assets/icono_juego.png")
pygame.display.set_icon(icon_image)

IMAGEN_MENU =  escalar_imagenes_fondo(f"{PATH}/Fondo_bordo.png",SIZE_SCREEN)
LOSE_IMAGE = escalar_imagenes_fondo(f"{PATH}/you_die.png",SIZE_SCREEN)
FONDO_PUNTAJE = escalar_imagenes_fondo(f"{PATH}/Fondo_puntaje.png",SIZE_SCREEN)
FONDO_JUGAR = escalar_imagenes_fondo(f"{PATH}/imagen_fondo_jugar.png",SIZE_SCREEN)
BANDERA = escalar_imagenes_fondo(f"{PATH}/bandera_mina.png",(20,20))
FONDO_NIVELES = escalar_imagenes_fondo(f"{PATH}/Fondo_selector_nivel.png",SIZE_SCREEN)
WIN_IMAGE = escalar_imagenes_fondo(f"{PATH}/you_win.png",SIZE_SCREEN)

# musica
WIN_MUSIC = pygame.mixer.Sound(f"{PATH}/Game Win.mp3")
WIN_MUSIC.set_volume(0.07)
LOSE_MUSIC = pygame.mixer.Sound(f"{PATH}/Game Over.mp3")
LOSE_MUSIC.set_volume(0.07)
JUGAR_MUSIC = pygame.mixer.Sound(f"{PATH}/wolf_play.mp3")
JUGAR_MUSIC.set_volume(0.07)
MENU_MUSIC = pygame.mixer.Sound(f"{PATH}/Toxicity.mp3")
MENU_MUSIC.set_volume(0.05)