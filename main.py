from settings import *
import pygame

pygame.init()

pygame.display.set_mode((window_hight, window_width))

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()