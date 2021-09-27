import pygame
from GMm import *

WIN_WIDTH = 1000
WIN_HEIGHT = 600
pygame.init()

window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("star")
zhong = star("A", 1e13, 600, 300, 0, 0)
zhong1 = star("A", 1e13, 400, 300, 0, 0)
star_1 = star("B", 1, 500, 300, 0, 2.58)
star_2 = star("B", 1, 300, 200, 2, -2)
stars_ = stars()
stars_.add(zhong)
stars_.add(zhong1)
window.fill((255, 255, 255))
FPS = 60
clock = pygame.time.Clock()
CREATE_ENEMY_EVENT = pygame.USEREVENT
pygame.time.set_timer(CREATE_ENEMY_EVENT, 100)


while True:
    clock.tick(FPS)
    pygame.draw.circle(window, (211, 211, 211), (star_1.x, star_1.y), 10)
    pygame.draw.circle(window, (0, 0, 0), (star_1.x, star_1.y), 5)
    pygame.draw.circle(window, (211, 211, 211), (star_2.x, star_2.y), 10)
    pygame.draw.circle(window, (0, 0, 0), (star_2.x, star_2.y), 5)
    pygame.draw.circle(window, (0, 0, 0), (zhong.x, zhong.y), 5)
    pygame.draw.circle(window, (0, 0, 0), (zhong1.x, zhong1.y), 5)
    pygame.display.update()
    stars_.gravitation(star_1)
    stars_.gravitation(star_2)
    pygame.draw.circle(window, (255, 255, 255), (star_1.x, star_1.y), 5)
    pygame.draw.circle(window, (255, 255, 255), (star_2.x, star_2.y), 5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == CREATE_ENEMY_EVENT:
            print(star_1.speed_x, star_1.speed_y, star_2.speed_x, star_2.speed_y)
