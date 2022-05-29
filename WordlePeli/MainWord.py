import random
import pygame
import time
from MoottoriWord import *
pygame.init()


näyttö = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()


sana = Random_sana()


kirj = Kirjaimet(näyttö,sana)

kirj.generate_laatikko()

while kirj.pyörii > 0:
    näyttö.fill((40,40,40))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            kirj.pyörii = 0
        if event.type == pygame.KEYDOWN :
            kirj.Katso_nappi_ja_kirjoita(event.key)
            if event.key == 13 and len(kirj.lista) == 5:
                kirj.Tarkistus()
                kirj.listat.append(lista_clear(kirj.lista))
        if event.type == pygame.MOUSEBUTTONDOWN:
            kirj.näpäytä_laatikkoa(event.pos)
    
    kirj.piirrä_kuutiot()
    kirj.piirrä_rivit()
    kirj.päivitä_näp()
    clock.tick(16)
    
    pygame.display.update()
time.sleep(2)
