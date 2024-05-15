import pygame

pygame.init()

width_and_height = (450,360)

window = pygame.display.set_mode(width_and_height)

mode = True
while mode:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            mode = False
            
pygame.quit()            