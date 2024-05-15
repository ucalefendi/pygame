import pygame

pygame.init()

width = 750
haight = 600
window = pygame.display.set_mode((width,haight))

white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
yellow = (255,255,0)

pygame.draw.line(window,red,(0,0),(150,250),5)
pygame.draw.line(window,blue,(150,250),(260,350),5)
pygame.draw.circle(window,yellow,(450,25),155,0)
pygame.draw.rect(window,red,(195,255,100,65),2)


mode = True
while mode:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mode = False
    pygame.display.update()        
            
            
pygame.quit()            