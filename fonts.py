import pygame

pygame.init()

window = pygame.display.set_mode((800,680))
font_list = pygame.font.get_fonts()
font_name = pygame.font.SysFont('futura',70)
writing = font_name.render('Hello,wellcome to our game',True,(255,0,0))
writing_koordinat = writing.get_rect()
writing_koordinat.topleft=(150,150)

# for font in font_list:
#     print(font)

mode = True
while mode:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mode = False
    window.blit(writing,writing_koordinat)
    pygame.display.update()        
            
            
pygame.quit()            