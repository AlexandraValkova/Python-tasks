class Rectangle:
    def __init__(self, a, b):
        self.length = a
        self.width = b

    def get_perimeter(self):
        return 2 * (self.length + self.width)


rect = Rectangle(7, 5)
print(rect.get_perimeter())