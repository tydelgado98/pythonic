import pygame

pygame.init()

screen = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("Pythonic")
clock = pygame.time.Clock()

img = pygame.image.load('./assets/picc.jpg')
pygame.display.set_icon(img)


test_surface = pygame.Surface((100, 200))
test_surface.fill('blue')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

   
    screen.blit(test_surface, (50, 50))
          

    pygame.display.update()
    clock.tick(60)