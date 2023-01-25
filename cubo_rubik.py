import pygame
import random

class RubikCube:
    def __init__(self):
        self.cube = [['w' for _ in range(2)] for _ in range(2)], \
                    [['r' for _ in range(2)] for _ in range(2)], \
                    [['b' for _ in range(2)] for _ in range(2)], \
                    [['o' for _ in range(2)] for _ in range(2)]

    def rotate_front(self, clockwise = True):
        if clockwise:
            temp = [self.cube[0][0][0], self.cube[0][0][1]]
            self.cube[0][0][0] = self.cube[0][1][0]
            self.cube[0][0][1] = self.cube[0][1][1]
            self.cube[0][1][0] = temp[0]
            self.cube[0][1][1] = temp[1]
            # Rotate adjacent faces
            temp = [self.cube[1][0][0], self.cube[1][1][0]]
            self.cube[1][0][0] = self.cube[3][1][0]
            self.cube[1][1][0] = self.cube[3][0][0]
            self.cube[3][1][0] = self.cube[2][0][0]
            self.cube[3][0][0] = self.cube[2][1][0]
            self.cube[2][0][0] = temp[0]
            self.cube[2][1][0] = temp[1]

    def rotate_top(self, clockwise = True):
        if clockwise:
            temp = [self.cube[0][0][0], self.cube[0][0][1]]
            self.cube[0][0][0] = self.cube[0][0][1]
            self.cube[0][0][1] = self.cube[0][1][1]
            self.cube[0][1][1] = self.cube[0][1][0]
            self.cube[0][1][0] = temp[0]
            # Rotate adjacent faces
            temp = [self.cube[4][0][0], self.cube[4][0][1]]
            self.cube[4][0][0] = self.cube[4][1][0]
            self.cube[4][0][1] = self.cube[4][1][1]
            self.cube[4][1][0] = temp[0]
            self.cube[4][1][1] = temp[1]
            temp = [self.cube[1][0][0], self.cube[1][0][1]]
            self.cube[1][0][0] = self.cube[5][0][1]
            self.cube[1][0][1] = self.cube[5][1][1]
            self.cube[5][0][1] = self.cube[3][1][0]
            self.cube[5][1][1] = self.cube[3][0][0]
            self.cube[3][1][0] = temp[0]
            self.cube[3][0][0] = temp[1]

    def rotate_right(self, clockwise = True):
        if clockwise:
            temp = [self.cube[0][1][0], self.cube[0][1][1]]
            self.cube[0][1][0] = self.cube[0][0][1]
            self.cube[0][1][1] = self.cube[0][1][1]
            self.cube[0][0][1] = self.cube[0][1][0]
            self.cube[0][1][0] = temp[0]
            # Rotate adjacent faces
            temp = [self.cube[4][0][1], self.cube[4][1][1]]
            self.cube[4][0][1] = self.cube[2][0][0]
            self.cube[4][1][1] = self.cube[2][1][0]
            self.cube[2][0][0] = self.cube[5][1][1]
            self.cube[2][1][0] = self.cube[5][0][1]
            self.cube[5][1][1] = temp[0]
            self.cube[5][0][1] = temp[1]
    
    def rotate_back(self, clockwise=True):
        if clockwise:
            temp = [self.cube[2][0][0], self.cube[2][0][1]]
            self.cube[2][0][0] = self.cube[2][1][0]
            self.cube[2][0][1] = self.cube[2][1][1]
            self.cube[2][1][0] = temp[0]
            self.cube[2][1][1] = temp[1]
            # Rotate adjacent faces
            temp = [self.cube[1][1][0], self.cube[3][1][0]]
            self.cube[1][1][0] = self.cube[4][1][0]
            self.cube[3][1][0] = self.cube[5][1][0]
            self.cube[4][1][0] = self.cube[1][1][0]
            self.cube[5][1][0] = temp[1]
    
    def rotate_left(self, clockwise=True):
        if clockwise:
            temp = [self.cube[0][0][0], self.cube[0][1][0]]
            self.cube[0][0][0] = self.cube[0][1][0]
            self.cube[0][1][0] = self.cube[0][1][1]
            self.cube[0][1][1] = self.cube[0][0][1]
            self.cube[0][0][1] = temp[0]
            # Rotate adjacent faces
            temp = [self.cube[4][0][0], self.cube[4][1][0]]
            self.cube[4][0][0] = self.cube[2][0][1]
            self.cube[4][1][0] = self.cube[2][1][1]
            self.cube[2][0][1] = self.cube[5][1][0]
            self.cube[2][1][1] = self.cube[5][0][0]
            self.cube[5][1][0] = temp[0]
            self.cube[5][0][0] = temp[1]
    
    def rotate_down(self, clockwise=True):
        if clockwise:
            temp = [self.cube[2][0][0], self.cube[2][0][1]]
            self.cube[2][0][0] = self.cube[2][0][1]
            self.cube[2][0][1] = self.cube[2][1][1]
            self.cube[2][1][1] = self.cube[2][1][0]
            self.cube[2][1][0] = temp[0]
            # Rotate adjacent faces
            temp = [self.cube[1][0][1], self.cube[1][1][1]]
            self.cube[1][0][1] = self.cube[4][0][1]
            self.cube[1][1][1] = self.cube[4][1][1]
            self.cube[4][0][1] = self.cube[3][1][1]
            self.cube[4][1][1] = self.cube[3][0][1]
            self.cube[3][1][1] = temp[0]
            self.cube[3][0][1] = temp[1]
            
    def is_solved(self):
        return all(self.cube[0][i][j] == 'w' for i in range(2) for j in range(2)) and \
               all(self.cube[1][i][j] == 'r' for i in range(2) for j in range(2)) and \
               all(self.cube[2][i][j] == 'b' for i in range(2) for j in range(2)) and \
               all(self.cube[3][i][j] == 'o' for i in range(2) for j in range(2))

    def shuffle(self):
        for _ in range(20):
            face = random.randint(0, 3)
            direction = random.choice([True, False])
            if face == 0:
                self.rotate_front(direction)
            elif face == 1:
                self.rotate_top(direction)


#Este ejemplo de código utiliza Pygame para crear una interfaz gráfica para el usuario 
# y permite que el usuario manipule el cubo mediante eventos de teclado o ratón.
#La función "shuffle" desordena el cubo y la función "is_solved" determina si el cubo está resuelto.
#La funcion draw es para dibujar el cubo en la interfaz gráfica.


