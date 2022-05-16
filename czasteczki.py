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
        self.g = 3
        self.polozenia_x = []
        self.polozenia_y = []
        self.katy = []
        self.czas_wznoszenia = 0
        self.prev_wznoszenia = 0
        self.czas_opadania = 0
        self.prev_opadania = 0
        self.wznoszenie = False
        self.opadanie = True
        self.v0 = 0

    def wyswietl(self):
        pygame.draw.circle(okno, self.kolor, (self.x, self.y), self.promien, 0)

    def ruch(self):
        """if self.predkosc_x > 0:
            self.predkosc_x -= self.opor
        if self.predkosc_x < 0.0000001:
            self.predkosc_x = 0"""

        self.x += math.cos(self.kat) * self.predkosc

        self.polozenia_x.append(self.x)

        if self.kat > 0:
            self.czas_opadania += 0.1
            self.y += self.g * self.czas_opadania

        if self.kat <= 0:
            print(self.prev_opadania)
            self.czas_wznoszenia += 0.1
            self.y -= self.prev_opadania * self.g - self.g * self.czas_wznoszenia

        self.polozenia_x.append(self.x)
        self.polozenia_y.append(self.y)

        if len(self.polozenia_x) > 1:
            wektorx = self.polozenia_x[len(self.polozenia_x)-1] - self.polozenia_x[len(self.polozenia_x)-2]
            wektory = self.polozenia_y[len(self.polozenia_y) - 1] - self.polozenia_y[len(self.polozenia_y) - 2]
            wektorv = math.sqrt(wektorx**2 + wektory**2)

            if wektorx != 0:
                self.kat = math.atan(wektory / wektorx)

        self.katy.append(self.kat)
        if 800 - self.promien - 30 < self.y < 800 - self.promien - 10:
            self.prev_opadania = self.czas_opadania

        if self.katy[len(self.katy) - 1] < self.katy[len(self.katy) - 2]:
            #self.prev_wznoszenia = self.czas_wznoszenia
            self.czas_wznoszenia = 0

        if self.katy[len(self.katy) - 1] > self.katy[len(self.katy) - 2]:
            #self.prev_opadania = self.czas_opadania
            self.czas_opadania = 0

    def odbicie(self):
        if self.y > 800 - self.promien - 20:
            self.kat = - self.kat

        if self.y < 0 + self.promien + 10:
            self.kat = - self.kat

        if self.x < 0 + self.promien + 10:
            self.kat = math.pi - self.kat

        if self.x > 1000 - self.promien - 10:
            self.kat = math.pi - self.kat
