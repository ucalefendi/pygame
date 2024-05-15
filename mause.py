import pygame
from char_move import monster,monster_koordinat

pygame.init()

window = pygame.display.set_mode((500,500))
monster_koordinat.topleft = (150,150)


mode = True
while mode:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mode = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x_value = event.pos[0]    
            mouse_y_value = event.pos[1]    
            monster_koordinat.x = mouse_x_value
            monster_koordinat.y = mouse_y_value
    
    window.fill((0,0,0))
    window.blit(monster,monster_koordinat)
    pygame.display.update()        
           
            
            
pygame.quit()            