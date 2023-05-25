class Ship:
    def __init__(self, bow, l, o):
        self.bow = bow
        self.l = l
        self.o = o
        self.lives = l

    @property
    def dots(self):
        ship_dots = []
        for i in range(self.l):
            cur_x = self.bow.x
            cur_y = self.bow.y

        if self.o == 0:
            cur_x += i
        elif self.o == 1:
            cur_y += i

        ship_dots.append(Dot(cur_x, cur_y))
