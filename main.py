import pygame

pygame.init()

screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Pythonic")
clock = pygame.time.Clock()

img = pygame.image.load('./assets/picc.jpg')
pygame.display.set_icon(img)


test_surface = pygame.Surface((100, 200))
test_surface.fill('red')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

   
    screen.blit(test_surface, (100, 100))
          

    pygame.display.update()
    clock.tick(60)