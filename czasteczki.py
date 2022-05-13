import math
import pygame

okno = pygame.display.set_mode((1000, 800))

class cząsteczka():
    def __init__(self, x, y, promien, predkosc, kąt):
        self.promien = promien
        self.kolor = (255, 0, 0)
        self.x = x
        self.y = y
        self.kąt = kąt
        self.predkosc = predkosc
        self.g = 0.9

    def wyswietl(self):
        pygame.draw.circle(okno, self.kolor, (self.x, self.y), self.promien, 0)

    def ruch(self):
        if self.kąt > 0 and self.kąt < math.pi:
            self.predkosc -= (self.g)
        if self.kąt > -math.pi and self.kąt < 0:
            self.predkosc += (self.g)
        self.x += math.cos(self.kąt) * self.predkosc
        self.y -= math.sin(self.kąt) * self.predkosc - 1.5*self.g



    def odbicie(self):
        if self.y > 800 - self.promien - 10:
            #self.y = 2 * (800 - self.promien - 10) - self.y
            self.kąt = - self.kąt

        if self.x < 0:
            self.kąt = math.pi - self.kąt

        if self.x > 1000:
            self.kąt = math.pi - self.kąt

