import pygame


size = 100


pygame.init()


width = size * 3
height = size * 4
screen = pygame.display.set_mode((width, height))

white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
orange = (255, 165, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)


pygame.draw.rect(screen, white, (size, size, size, size))


pygame.draw.rect(screen, red, (0, size, size, size))


pygame.draw.rect(screen, blue, (size * 2, size, size, size))


pygame.draw.rect(screen, orange, (size, size * 2, size, size))


pygame.draw.rect(screen, green, (size, 0, size, size))


pygame.draw.rect(screen, yellow, (size * 2, 0, size, size))


pygame.display.flip()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()

# este programa te enseña la representacion de 
# una cara de un cubo 3x3 en pygame