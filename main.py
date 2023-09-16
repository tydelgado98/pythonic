import pygame

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Pythonic")
clock = pygame.time.Clock()

img = pygame.image.load('./assets/picc.jpg')
pygame.display.set_icon(img)
test_font = pygame.font.Font('font/pixeltype.ttf' , 40)
text_surface = test_font.render('My Game', False, 'blue')


test_surface = pygame.image.load('./assets/Sky.png')
# test_surface = pygame.Surface((800,300))
# test_surface.fill(('indigo'))
test_ground = pygame.image.load('./assets/ground.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

   
    screen.blit(test_surface, (0, 0))
    screen.blit(test_ground, (0, 300))
    screen.blit(text_surface, (350, 50))
          

    pygame.display.update()
    clock.tick(60)