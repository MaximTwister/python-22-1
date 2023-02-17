# Polymorphism
# str int

class T1:
    def __init__(self):
        self.n = 10

    def total(self, x) -> int:
        return self.n + int(x)


class T2:
    def __init__(self):
        self.n = "maksym"

    def total(self, x, y) -> int:
        return len(self.n  + str(x))


print([instance.total("5") for instance in (T1(), T2())])
