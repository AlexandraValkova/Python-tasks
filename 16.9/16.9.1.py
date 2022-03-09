class Parallelogram:
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h

    def __str__(self):
        return f"Parallelogram({self.a}, {self.b}, {self.h})"


par = Parallelogram(2, 3, 4)
print(par)