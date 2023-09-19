import pygame

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Pythonic")
clock = pygame.time.Clock()

img = pygame.image.load('./assets/picc.jpg')
pygame.display.set_icon(img)

# Font
test_font = pygame.font.Font('font/pixeltype.ttf' , 40)
text_surface = test_font.render('Pythonic', False, 'blue')

# Images
test_surface = pygame.image.load('./assets/Sky.png')
test_ground = pygame.image.load('./assets/ground.png')
snail_surface = pygame.image.load('./assets/snail1.png')


snail_x_pos = 800


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

   
    screen.blit(test_surface, (0, 0))
    screen.blit(test_ground, (0, 300))
    screen.blit(text_surface, (350, 50))
     # that means that the snail will move 3 pixels to the left
    snail_x_pos -= 3 
    if snail_x_pos < -100 :
     # that means that the snail will move to the right side of the screen
        snail_x_pos = 800
     # the 264 is the y position of the snail
    screen.blit(snail_surface, (snail_x_pos, 264))
   
          

    pygame.display.update()
    clock.tick(60)