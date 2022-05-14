import math
import pygame

okno = pygame.display.set_mode((1000, 800))

class cząsteczka():
    def __init__(self, x, y, promien, predkosc, kąt):
        self.promien = promien
        self.kolor = (255, 0, 0)
        self.y_poczatkowe = y
        self.x = x
        self.y = y
        self.kąt = kąt
        self.predkosc_x = predkosc
        self.predkosc_y = 0
        self.g = 4
        self.polozenia_x = []
        self.polozenia_y = []
        self.czas = 0
        self.opor = 0.1

    def wyswietl(self):
        pygame.draw.circle(okno, self.kolor, (self.x, self.y), self.promien, 0)

    def ruch(self):
        if self.predkosc_x > 0:
            self.predkosc_x -= self.opor
        if self.predkosc_x < 0.0000001:
            self.predkosc_x = 0


        self.x += math.cos(self.kąt) * self.predkosc_x
        self.y -= math.sin(self.kąt) * self.predkosc_x - 1.5 * self.g

        print('x = ' + str(self.x))
        print('y = ' + str(self.y))
        print('alfa = ' + str(self.kąt))

        self.polozenia_x.append(self.x)
        self.polozenia_y.append(self.y)


        if len(self.polozenia_x) > 1:
            wektorx = self.polozenia_x[len(self.polozenia_x)-1] - self.polozenia_x[len(self.polozenia_x)-2]
            wektory = self.polozenia_y[len(self.polozenia_y) - 1] - self.polozenia_y[len(self.polozenia_y) - 2]
            wektorv = math.sqrt(wektorx**2 + wektory**2)
            self.kąt = math.asin(wektory/wektorx)
    def odbicie(self):
        if self.y > 800 - self.promien:
            #self.y = 2 * (800 - self.promien - 10) - self.y
            self.kąt = - self.kąt

        #if self.y > 800 - self.promien + 5:
            #self.y = 800 - self.promien + int(0.04*self.promien)

        if self.x < 0:
            self.kąt = math.pi - self.kąt

        if self.x > 1000:
            self.kąt = math.pi - self.kąt

