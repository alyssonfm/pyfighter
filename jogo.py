from projeto2 import *

pygame.init()

b = Background()

grupo = RenderUpdates()
p1 = Personagem('movimento6.png','movimento4.png', Vector2(600,400))
p2 = Personagem('muv1.png','muv0.png', Vector2(100, 400))

texto = Texto()

 
clock = pygame.time.Clock()

while True:


    key_direction = Vector2(0, 0)
    key_direction2 = Vector2(0, 0)

    pressed_keys = pygame.key.get_pressed()



    for event in pygame.event.get():
        if event.type == QUIT or (pressed_keys[K_LALT] and pressed_keys[K_F4]):
            pygame.quit()
 
    p1.movimentos(pressed_keys, p2)
    p2.movimentos(pressed_keys, p1, esquerda = K_a, direita = K_d, cima = K_w, baixo = K_s)

 
    b.screen.blit(b.background, (0,0))
    
    b.screen.blit(p1.borda, (19, 29))
    b.screen.blit(p2.borda, (479,29))

    
    for i in range(p1.life):
      b.screen.blit(p1.hp, (12*i + 20, 30))
    for j in range(p2.life):
      b.screen.blit(p2.hp, (12*j + 480,30))

    if pressed_keys[K_KP0]:
        b.screen.blit(p1.image2, p1.sprite_pos)
        if p1.rect2.colliderect(p2.rect) and (p2.sprite_pos.x - p2.largura_imagem) < p1.sprite_pos.x < (p2.sprite_pos.x + p2.largura_imagem):
            p1.life -= 1
    else:
        b.screen.blit(p1.image, p1.sprite_pos)

    if pressed_keys[K_u]:
        b.screen.blit(p2.image2, p2.sprite_pos)
        if p2.rect2.colliderect(p1.rect) and (p1.sprite_pos.x - p1.largura_imagem) < p2.sprite_pos.x < (p1.sprite_pos.x + p1.largura_imagem):
            p2.life -= 1
    else:
        b.screen.blit(p2.image, p2.sprite_pos)


    if texto.t >= 0:
            texto.imprime(b.screen, 'PyFighter!', (340,0))
            texto.imprime(b.screen, 'Player 1', (10,0))
            texto.imprime(b.screen, 'Player 2', (700,0))
            texto.imprime_tempo(b.screen)
            texto.tempo -= 1
            
    else:
        if p1.life > p2.life:
            texto.imprime(b.screen, 'Player 1 Venceu', (350,250))

        elif p1.life < p2.life:
            texto.imprime(b.screen, 'Player 2 Venceu', (350,250))
        else:
            texto.imprime(b.screen, 'Game Over', (350,250))
 
    time_passed = clock.tick(60)
    time_passed_seconds = time_passed / 1000.0
    
    p1.sprite_pos += p1.key_direction * p1.sprite_speed * time_passed_seconds
    p2.sprite_pos += p2.key_direction * p2.sprite_speed * time_passed_seconds

    pygame.display.update()
