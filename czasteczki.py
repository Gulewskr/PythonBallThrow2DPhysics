import math
import pygame

okno = pygame.display.set_mode((1000, 800))

class cząsteczka():
    def __init__(self, x, y, promien, predkosc, kat):
        self.promien = promien
        self.kolor = (255, 0, 0)
        self.x = x
        self.y = y
        self.kat = kat
        self.predkosc = predkosc
        self.predkosc_x = 0
        self.predkosc_y = 0
        self.g = 0.9
        self.polozenia_x = []
        self.polozenia_y = []
        self.opor = 0.5

    def wyswietl(self):
        pygame.draw.circle(okno, self.kolor, (self.x, self.y), self.promien, 0)

    def ruch(self):
        '''if self.predkosc_x > 0:
            self.predkosc_x -= self.opor
        if self.predkosc_x < 0.0000001:
            self.predkosc_x = 0**'''

        self.predkosc_x = math.cos(self.kat) * self.predkosc
        self.predkosc_y = math.sin(self.kat) * self.predkosc

        if self.kat > 0:
            self.predkosc_y += self.g

        if self.kat < 0:
            self.predkosc_y -= self.g

        print(self.kat)

        self.x += self.predkosc_x
        self.y += self.predkosc_y

        self.polozenia_x.append(self.x)
        self.polozenia_y.append(self.y)

        if len(self.polozenia_x) > 1:
            wektorx = self.polozenia_x[len(self.polozenia_x)-1] - self.polozenia_x[len(self.polozenia_x)-2]
            wektory = self.polozenia_y[len(self.polozenia_y) - 1] - self.polozenia_y[len(self.polozenia_y) - 2]
            wektorv = math.sqrt(wektorx**2 + wektory**2)
            if wektorx != 0:
                self.kat = math.atan(wektory / wektorx)

    def odbicie(self):
        if self.y > 800 - self.promien - 10:
            self.kat = - self.kat

        if self.y < 0 + self.promien + 10:
            self.kat = - self.kat

        if self.x < 0:
            self.kat = math.pi - self.kat

        if self.x > 1000:
            self.kat = math.pi - self.kat

