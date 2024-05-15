import pygame

pygame.init()

window = pygame.display.set_mode((800,800))
monster = pygame.image.load("monster.png")
monster_koordinat = monster.get_rect()
monster_koordinat.topleft =(800/2,800/2)

speed = 50

mode = True
while mode:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mode = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:    
                monster_koordinat.x -= speed
            elif event.key == pygame.K_UP:
                monster_koordinat.y -= speed
            elif event.key == pygame.K_RIGHT:
                monster_koordinat.x += speed
            elif event.key == pygame.K_DOWN:
                monster_koordinat.y += speed            
    window.fill((0,0,0))        
    window.blit(monster,monster_koordinat) 
    pygame.display.update()       
pygame.quit()            