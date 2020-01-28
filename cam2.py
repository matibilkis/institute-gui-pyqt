import pygame
import pygame.camera
from pygame.locals import *
import os

class tomofoto(object):
    def __init__(self,nombre):
        FILENAME=str(nombre)
        DEVICE = '/dev/video0'
        SIZE=(640,480)
        pygame.init()
        pygame.camera.init()
        display = pygame.display.set_mode(SIZE, 0)
        camera = pygame.camera.Camera(DEVICE, SIZE)
        camera.start()
        screen = pygame.surface.Surface(SIZE, 0, display)
        capture = True
        while capture:
            screen = camera.get_image(screen)
            display.blit(screen, (0,0))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == KEYDOWN and event.key == K_s:
                    os.chdir("imagenes")
                    print("guardado")
                    pygame.image.save(screen, FILENAME)
                    os.chdir("..")
                    capture=False

        camera.stop()
        pygame.quit()
        return
