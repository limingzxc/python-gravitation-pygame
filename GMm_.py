G = 6.67e-11
WIN_WIDTH = 1000
WIN_HEIGHT = 600


def speed_v(M, x, y):
    return (G * M / ((x ** 2 + y ** 2) ** 0.5)) ** 0.5


class star:
    def __init__(self, li):
        self.m = li[0]
        self.x = li[1]
        self.y = li[2]
        self.speed_x = li[3]
        self.speed_y = li[4]

    def motion(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def acceleration(self, q_x, q_y):
        self.speed_x += q_x
        self.speed_y += q_y


class stars:
    def __init__(self):
        self.li = []

    def add(self, star_):
        self.li.append(star_)

    def gravitation(self, star_):
        a = 0
        b = 0
        for i in self.li:
            if i == star_:
                continue
            else:
                x = i.x - star_.x
                y = i.y - star_.y
                r = (x ** 2 + y ** 2) ** 0.5
                q = G * i.m / r ** 2
                a += x / r * q
                b += y / r * q
        star_.acceleration(a, b)
        star_.motion()
