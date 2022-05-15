import math
import pygame

okno = pygame.display.set_mode((1000, 800))

class cząsteczka():
    def __init__(self, x, y, promien, predkosc, kat):
        self.promien = promien
        self.kolor = (255, 0, 0)
        self.y_poczatkowe = y
        self.x = x
        self.y = y
        self.kat = kat
        self.kat_poczatkowy = kat
        self.predkosc_x = predkosc
        self.predkosc_y = 0
        self.g = 0.4
        self.polozenia_x = []
        self.polozenia_y = []
        self.czas = 0
        self.opor = 0.1

    def wyswietl(self):
        pygame.draw.circle(okno, self.kolor, (self.x, self.y), self.promien, 0)

    def ruch(self):
        self.czas += 0.1

        '''if self.predkosc_x > 0:
            self.predkosc_x -= self.opor
        if self.predkosc_x < 0.0000001:
            self.predkosc_x = 0**'''

        self.x += math.cos(self.kat_poczatkowy) * self.predkosc_x

        if self.kat >= 0:
            #self.y -= math.sin(self.kąt) * self.predkosc_x
            self.y += self.g*(self.czas**2)

        if self.kat < 0:
            self.y -= self.g*(self.czas**2)


        self.polozenia_x.append(self.x)
        self.polozenia_y.append(self.y)

        if len(self.polozenia_x) > 1:
            wektorx = self.polozenia_x[len(self.polozenia_x)-1] - self.polozenia_x[len(self.polozenia_x)-2]
            wektory = self.polozenia_y[len(self.polozenia_y) - 1] - self.polozenia_y[len(self.polozenia_y) - 2]
            wektorv = math.sqrt(wektorx**2 + wektory**2)
            if wektorx != 0:
                self.kat = math.atan(wektory / wektorx)

    def odbicie(self):
        if self.y > 800 - self.promien:
            #self.y = 2 * (800 - self.promien - 10) - self.y
            self.kat = - self.kat
            self.kat_poczatkowy = - self.kat_poczatkowy

        if self.y < 0 + self.promien:
            self.kat = - self.kat
            self.kat = - self.kat_poczatkowy

        #if self.y > 800 - self.promien + 5:
            #self.y = 800 - self.promien + int(0.04*self.promien)

        if self.x < 0:
            self.kat = math.pi - self.kat

        if self.x > 1000:
            self.kat = math.pi - self.kat

