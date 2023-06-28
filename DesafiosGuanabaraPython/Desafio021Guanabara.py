# Faça um programa que abra e reproduza o áudio de um arquivo mp3 #

import pygame
import sys

pygame.init()
pygame.mixer.music.load('Sutekimeppou.mp3')
pygame.mixer.music.play()

end_event = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(end_event)

while True:
    for event in pygame.event.get():
        if event.type == end_event:
            pygame.mixer.music.stop()
            pygame.quit()
            sys.exit()