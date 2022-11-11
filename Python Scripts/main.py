import pygame as pg
import level
import sys
from Settings import settings as game

# initialize pygame
pg.init()

# creating the canvas/screen
menu = game.menu_size
screen = pg.display.set_mode(menu)
pg.display.set_caption("Ray Caster 3D")
pg.display.flip()


def startMenu():
    BUFFER = 50
    BUTTON_W = 2 / 3 * game.MENU_WIDTH
    BUTTON_H = (2/3 * game.MENU_HEIGHT) / 3 - BUFFER
    bx = (game.MENU_WIDTH - BUTTON_W) / 2
    by = (game.MENU_HEIGHT - (BUTTON_H*3 + BUFFER*2)) / 2
    small_bx = (bx / 2) - BUFFER

    # play game button
    pg.draw.rect(screen, game.RED, pg.Rect(bx, by, BUTTON_W, BUTTON_H))
    font = pg.font.SysFont(None, 24)
    play = font.render('New Game', True, game.BLACK)
    txt_x = bx + BUTTON_W/2 - play.get_rect().width/2
    txt_y = by + BUTTON_H/2 - play.get_rect().height/2
    screen.blit(play, (txt_x, txt_y))

    # load game button
    load_y = by + BUTTON_H + BUFFER/2
    pg.draw.rect(screen, game.RED, pg.Rect(bx, load_y, BUTTON_W, BUTTON_H))
    font = pg.font.SysFont(None, 24)
    load = font.render('Load Game', True, game.BLACK)
    load_txt_y = load_y + BUTTON_H / 2 - load.get_rect().height / 2
    screen.blit(load, (txt_x, load_txt_y))

    # options button
    quit_y = load_y + BUTTON_H + BUFFER/2
    pg.draw.rect(screen, game.RED, pg.Rect(bx, quit_y, BUTTON_W/2 - BUFFER/5, BUTTON_H))
    font = pg.font.SysFont(None, 24)
    opt = font.render('Options', True, game.BLACK)
    txt_x = bx + BUTTON_W / 2 - opt.get_rect().width / 2
    opt_txt_x = txt_x - BUTTON_W / 4 - 5
    quit_txt_y = quit_y + BUTTON_H / 2 - opt.get_rect().height / 2
    screen.blit(opt, (opt_txt_x, quit_txt_y))

    # quit button
    pg.draw.rect(screen, game.RED, pg.Rect(bx + BUTTON_W/2 + BUFFER/5, quit_y, BUTTON_W / 2 - BUFFER / 5, BUTTON_H))
    font = pg.font.SysFont(None, 24)
    qt = font.render('Quit', True, game.BLACK)
    quit_txt_x = bx + BUTTON_W/2 - qt.get_rect().width/2 + BUTTON_W/4 + 3
    screen.blit(qt, (quit_txt_x, quit_txt_y))


def start():
    startMenu()
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit(0)

        pg.display.update()


if __name__ == '__main__':
    start()
