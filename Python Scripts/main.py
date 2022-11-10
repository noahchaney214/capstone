import pygame as pg
import level
import sys
from UI import settings as game

# initialize pygame
pg.init()

# creating the canvas/screen
screen = pg.display.set_mode(game.menu_size)
pg.display.set_caption("Ray Caster 3D")
pg.display.flip()


def start():
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit(0)

        pg.display.update()


if __name__ == '__main__':
    start()
