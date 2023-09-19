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
sky_surface = pygame.image.load('./assets/Sky.png').convert()
game_ground = pygame.image.load('./assets/ground.png').convert()

# character images
snail_surface = pygame.image.load('./assets/snail1.png').convert_alpha()
player_surface = pygame.image.load('./assets/player_stand.png').convert_alpha()

# rectangles
snail_rect = snail_surface.get_rect(midbottom = (800, 300))
player_rect = player_surface.get_rect(midbottom = (80, 300))




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.blit(sky_surface, (0, 0))
    screen.blit(game_ground, (0, 300))
    screen.blit(text_surface, (350, 50))

     # that means that the snail will move 3 pixels to the left
    snail_rect.right -= 3 
    if snail_rect.left <= 0:
     # that means that the snail will move to the right side of the screen
        snail_rect.left = 800
     # the 264 is the y position of the snail
    screen.blit(snail_surface, snail_rect)
    print(player_rect.left)
    screen.blit(player_surface, player_rect)
   
          

    pygame.display.update()
    clock.tick(60)