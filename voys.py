import pygame

pygame.init()

window = pygame.display.set_mode((500,500))
voys_effect1 = pygame.mixer.Sound("voys1.wav")
voys_effect2 = pygame.mixer.Sound("voys2.wav")
voys_effect3 = pygame.mixer.Sound("voys3.wav")

voys_effect1.play()
pygame.time.delay(1000)
voys_effect2.play()
pygame.time.delay(1000)
pygame.mixer.music.load("voys3.wav")
pygame.mixer.music.play(-1,0.0)



mode =True
while mode:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            mode = False
            
pygame.quit()            