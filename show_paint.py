import pygame

pygame.init()

width = 640
haight = 480
window = pygame.display.set_mode((width,haight))
monster = pygame.image.load('monster.png')
monster_koordinat = monster.get_rect()
monster_koordinat.topleft = (10,10)

white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
yellow = (255,255,0)


mode = True
while mode:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mode = False
    
    window.blit(monster,monster_koordinat)
    pygame.display.update()       
            
            
pygame.quit()            