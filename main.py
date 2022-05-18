import pygame
import czasteczki
import math

background = pygame.image.load('background.png')

if __name__ == '__main__':
    pygame.init()
    okno = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption("Symulacja zderzeń")
#                                      x    y    r   v    alfa
    Czasteczka = czasteczki.cząsteczka(500, 400, 40, 15, 0.25*math.pi)
    clock = pygame.time.Clock()


    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        okno.blit(background, (0, 0))

        Czasteczka.ruch()
        Czasteczka.odbicie()
        Czasteczka.wyswietl()
        pygame.display.flip()
