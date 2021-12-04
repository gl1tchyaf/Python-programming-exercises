class circle(object):
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14


aCircle = circle(2)
print(aCircle.area())

