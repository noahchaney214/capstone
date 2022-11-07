import pygame as pg
import numpy as np
import level
from Settings import settings as game

# initialize pygame
pg.init()

# creating the canvas/screen
screen = pg.display.set_mode(game.size)
pg.display.set_caption("Ray Caster 3D")
pg.display.flip()

exit = False

# hello
def start(self):
    currentLevel = 1

    print(level.LEVEL[currentLevel])

    currentLevel += 1

    print(level.LEVEL[currentLevel])

    while not exit:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit = True

        pg.display.update()


if __name__ == '__main__':
    start()
