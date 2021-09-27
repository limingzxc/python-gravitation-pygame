import pygame

WIN_WIDTH = 1000
WIN_HEIGHT = 600
pygame.init()

window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("star")
G = 6.67e-11
M = 1e13
x = 400
y = 300
x1 = 200
y1 = 200
window.fill((255, 255, 255))
FPS = 60
clock = pygame.time.Clock()
speed_x = 0  # 1
# speed_y = 3
speed_y = (G*M/(((WIN_WIDTH/2 - x) ** 2 + (WIN_HEIGHT/2 - y) ** 2) ** 0.5))**0.5
speed_x1 = 0.5
speed_y1 = -1
CREATE_ENEMY_EVENT = pygame.USEREVENT
pygame.time.set_timer(CREATE_ENEMY_EVENT, 100)


def gravitation(a, b, c, d):
    x_ = WIN_WIDTH / 2 - c
    y_ = WIN_HEIGHT / 2 - d
    r = (x_ ** 2 + y_ ** 2) ** 0.5
    q = G * M / r ** 2
    a += x_/r * q
    b += y_/r * q
    return a, b


while True:
    clock.tick(FPS)
    pygame.draw.circle(window, (211, 211, 211), (x, y), 10)
    pygame.draw.circle(window, (0, 0, 0), (x, y), 5)
    pygame.draw.circle(window, (211, 211, 211), (x1, y1), 10)
    pygame.draw.circle(window, (0, 0, 0), (x1, y1), 5)
    speed_x, speed_y = gravitation(speed_x, speed_y, x, y)
    speed_x1, speed_y1 = gravitation(speed_x1, speed_y1, x1, y1)
    x += speed_x
    y += speed_y
    x1 += speed_x1
    y1 += speed_y1
    pygame.draw.circle(window, (0, 0, 0), (WIN_WIDTH / 2, WIN_HEIGHT / 2), 5)
    pygame.display.update()
    pygame.draw.circle(window, (255, 255, 255), (x, y), 5)
    pygame.draw.circle(window, (255, 255, 255), (x1, y1), 5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == CREATE_ENEMY_EVENT:
            print(speed_x, speed_y, speed_x1, speed_y1)
