import math

class Rectangle:
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def area(self):
        return self.length * self.width

class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return math.pi * self.radius ** 2

if __name__ == "__main__":
    q = int(input())
    queries = []
    for _ in range(q):
        args = input().split()
        shape_name, params = args[0], list(map(int, args[1:]))

        if shape_name == "rectangle":
            a, b = params[0], params[1]
            shape = Rectangle(a, b)
        elif shape_name == "circle":
            r = params[0]
            shape = Circle(r)
        else:
            raise ValueError("invalid shape type")

        area_result = shape.area()
        print("{:.2f}".format(area_result))


