import pygame
from pygame.locals import *

class Menu:
  def __init__(self, indice = 1):
    self.menus = {1: pygame.image.load('pyfighter1.1.2.PNG'),
                  2: pygame.image.load('pyfighter2.2.2.PNG'),
                  3: pygame.image.load('pyfighter3.3.2.PNG')}
    self.indice = indice
  def menu(self, indice):
    return self.menus[indice]


menu = Menu()

screen =  pygame.display.set_mode((800,600),0,32)
pygame.display.set_caption("Teste")
back = menu.menu(1)

menu_atividade = True
while menu_atividade:
  for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                if menu.indice == 1:
                    menu.indice = 3
                else:
                    menu.indice -= 1
                back = menu.menu(menu.indice)
            if event.key == K_DOWN:
                if menu.indice == 3:
                    menu.indice = 1
                else:
                    menu.indice += 1
                back = menu.menu(menu.indice)
            if event.key == K_RETURN:
                if menu.indice == 3:
                    pygame.quit()
                elif menu.indice == 1:
                    menu_atividade = False
                    from jogo import *

  screen.blit(back, (0,0))
  pygame.display.update()
