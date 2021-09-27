G = 6.67e-11


class star:
    def __init__(self, type_, m, x, y, speed_x, speed_y):
        self.type_ = type_
        self.m = m
        self.x = x
        self.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y

    def motion(self):
        if self.type_ == "B":
            self.x += self.speed_x
            self.y += self.speed_y

    def acceleration(self, q_x, q_y):
        if self.type_ == "B":
            self.speed_x += q_x
            self.speed_y += q_y


class stars:
    def __init__(self):
        self.li = []

    def add(self, star_):
        if star_.type_ == "A":
            self.li.append(star_)
        else:
            print("B类星球不能添加")

    def gravitation(self, star_):
        a = 0
        b = 0
        for i in self.li:
            x = i.x - star_.x
            y = i.y - star_.y
            r = (x ** 2 + y ** 2) ** 0.5
            q = G * i.m / r ** 2
            a += x / r * q
            b += y / r * q
        star_.acceleration(a, b)
        star_.motion()
