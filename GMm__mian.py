import pygame
from GMm_ import *
pygame.init()

m1 = [1, 700, 300, 0, 0]
m2 = [1e14, 500, 300, 0, 0]
m3 = [1, 300, 300, 0, 0]
m1[4] = speed_v(m2[0], m1[1]-m2[1], m1[2]-m2[2])
m3[4] = -speed_v(m2[0], m3[1]-m2[1], m3[2]-m2[2])

window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("star")

zhong = star(m1)
zhong1 = star(m2)
diqiou = star(m3)
stars_ = stars()
stars_.add(zhong)
stars_.add(zhong1)
stars_.add(diqiou)

window.fill((255, 255, 255))
FPS = 60
clock = pygame.time.Clock()
CREATE_ENEMY_EVENT = pygame.USEREVENT
pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)


while True:

    clock.tick(FPS)

    pygame.draw.circle(window, (211, 211, 211), (zhong.x, zhong.y), 10)
    pygame.draw.circle(window, (0, 0, 0), (zhong.x, zhong.y), 5)
    pygame.draw.circle(window, (211, 211, 211), (zhong1.x, zhong1.y), 10)
    pygame.draw.circle(window, (0, 0, 0), (zhong1.x, zhong1.y), 5)
    pygame.draw.circle(window, (211, 211, 211), (diqiou.x, diqiou.y), 10)
    pygame.draw.circle(window, (0, 0, 0), (diqiou.x, diqiou.y), 5)

    pygame.display.update()

    pygame.draw.circle(window, (211, 211, 211), (zhong.x, zhong.y), 5)
    pygame.draw.circle(window, (211, 211, 211), (zhong1.x, zhong1.y), 5)
    pygame.draw.circle(window, (211, 211, 211), (diqiou.x, diqiou.y), 5)

    stars_.gravitation(zhong)
    stars_.gravitation(zhong1)
    stars_.gravitation(diqiou)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            exit()

        elif event.type == CREATE_ENEMY_EVENT:
            print(zhong.speed_x, zhong.speed_y, zhong1.speed_x, zhong1.speed_y, diqiou.speed_x, diqiou.speed_y)
