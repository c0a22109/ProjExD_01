import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    k_img = pg.image.load("ex01/fig/3.png")
    k_img = pg.transform.flip(k_img, True, False)
    k_imgs =[k_img, pg.transform.rotozoom(k_img, 10, 1.0)]
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [0, 0])
        if tmr % 2 == 0 :
            screen.blit(k_imgs[1], [300, 200])
        else:
            screen.blit(k_imgs[0], [300, 200])        
        pg.display.update()
        tmr += 1        
        clock.tick(5)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()