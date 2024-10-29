import pygame
import random

pygame.init()

#janela
largura=640
altura=420
tela=pygame.display.set_mode((largura, altura))
pygame.display.set_caption("rpg")

#loop
rodando=True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando=False
            
pygame.quit()

            