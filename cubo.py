import pygame
import sys
from cubo_rubik import RubikCube


# Inicializar pygame
pygame.init()

# Configurar la ventana
size = (500, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Rubik's Cube")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

color_map = {
    'w': WHITE,
    'r': RED,
    'b': BLUE,
    'o': ORANGE,
}

def draw(cube, screen):
    for idx, face in enumerate(cube.cube):
        for i in range(2):
            for j in range(2):
                color = color_map[face[i][j]]
                pygame.draw.rect(screen, color, [50 * (idx + 1) + 50 * j, 50 * (i + 1), 50, 50])
                pygame.draw.rect(screen, BLACK, [50 * (idx + 1) + 50 * j, 50 * (i + 1), 50, 50], 1)

def main():
    clock = pygame.time.Clock()
    cube = RubikCube()

    running = True
    while running:
        screen.fill(BLACK)
        draw(cube, screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    cube.rotate_front()
                elif event.key == pygame.K_t:
                    cube.rotate_top()
                elif event.key == pygame.K_r:
                    cube.rotate_right()
                elif event.key == pygame.K_b:
                    cube.rotate_back()
                elif event.key == pygame.K_l:
                    cube.rotate_left()
                elif event.key == pygame.K_d:
                    cube.rotate_down()
                elif event.key == pygame.K_s:
                    cube.shuffle()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()

# En este ejemplo, hemos configurado una ventana de 500x500 píxeles, y mapeamos cada letra 
# de color a su valor RGB correspondiente. La función draw() se encarga de dibujar el cubo en la ventana.

# En el bucle principal, se llama a la función draw() para actualizar la pantalla, y 
# luego se manejan los eventos de teclado. Por ejemplo, cuando se presiona la tecla 'f', 
# se llama a cube.rotate_front(). De manera similar, se asignan otras teclas a las funciones de 
# rotación restantes.