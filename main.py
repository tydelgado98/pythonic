import pygame

pygame.init()

screen = pygame.display.set_mode((1080, 1920))
pygame.display.set_caption("Pythonic")

img = pygame.image.load('./assets/picc.jpg')
pygame.display.set_icon(img)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()