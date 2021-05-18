import pygame
from pygame.locals import *
from vector2 import *

pygame.init()

screen = pygame.display.set_mode((800,600), 0, 16)
back = pygame.image.load('pyfighter.png')

while True:                    
    pos = pygame.mouse.get_pos()
    pos_x = pos[0]
    pos_y = pos[1]
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        elif event.type == MOUSEBUTTONUP:
            if (34 < pos_x < 170) and (301 < pos_y < 318):
                from projeto2 import *
                #selecao de cenarios
            elif (57 < pos_x < 138) and (328 < pos_y < 340):
                pass
                #opcoes
            elif (76 < pos_x < 122) and (353 < pos_y < 366):
                pygame.quit()

    screen.blit(back, (0,0))
    pygame.display.update()
        
