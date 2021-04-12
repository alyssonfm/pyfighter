import pygame
from pygame.locals import *
from vector2 import *
from pygame.sprite import *
from pygame.rect import *

class Texto:
    def __init__(self):
        self.tempo = 8000
        self.font = pygame.font.Font("Kingthings Trypewriter.ttf", 20)
        self.t = 0
        
    def imprime(self,screen, texto ,pos):
        text_surface = self.font.render(texto, True, (255,255,255))
        screen.blit(text_surface,(pos))
        
    def imprime_tempo(self, screen):
        self.t = int(self.tempo)/80
        text_surface = self.font.render(str(self.t), True, (255,255,255))
        screen.blit(text_surface,(380,30))
     
class Personagem(Sprite):
    def __init__(self, imagem = '', imagem2 = '', sprite_pos = ''):
        Sprite.__init__(self)
        pygame.rect.Rect.collidedict.__init__()
        self.life = 25
        self.image = pygame.image.load(imagem).convert_alpha()
        self.image2 = pygame.image.load(imagem2).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect2 = self.image2.get_rect()
        self.hp = self.barra(10,40,(255,0,0))
        self.borda = self.barra(302,42,(192,192,192))
        self.sprite_pos = sprite_pos
        self.largura_imagem= self.image.get_width()
        self.altura_imagem = self.image.get_height()
        self.key_direction = Vector2(0, 0)
        self.sprite_speed= 300.
        self.ant = 0
        
    def barra(self,largura, altura, cor = (255,255,255)):
        surface = pygame.surface.Surface((largura, altura), 0)
        for x in range(largura):
            retangulo = Rect(x, 0, 1, altura)
            pygame.draw.rect(surface, cor, retangulo, 0)
        return surface
    
    def movimentos(self,pressed_keys, outro, esquerda = K_LEFT, direita = K_RIGHT, cima = K_UP, baixo = K_DOWN):
        if pressed_keys[esquerda] and  (self.sprite_pos.x) >= 0:
            self.key_direction.x = -1
        
        elif pressed_keys[direita] and (self.sprite_pos.x + self.largura_imagem) <= 800:
            self.key_direction.x = +1

           
        else:
            self.key_direction.x = 0
        
        if pressed_keys[cima] and self.sprite_pos.y >= 0:
            self.key_direction.y = -1
         
        elif pressed_keys[baixo] and (self.sprite_pos.y + self.altura_imagem) <= 600:
            self.key_direction.y = +1
            
        else:
            self.key_direction.y = 0

        self.key_direction.normalize()
        


class Background:
    def __init__(self,imagem = 'fundo.jpg',tamanho_tela = (800,600)):
        self.screen = pygame.display.set_mode(tamanho_tela, 0, 16)
        titulo = pygame.display.set_caption('PyFighter 1.0')
        self.background = pygame.image.load(imagem).convert()





