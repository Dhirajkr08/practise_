class Shape:
    def typeshape(self):
        print("This is shape")
class rectangle(Shape):
    def rectangeShape(self):
        print("This is rectangle shape")
class circle(Shape):
    def circularShape(self):
        print("this is circular shape")
class square(rectangle):
    def squareShape(self):
        print("Square is Rectangle")
s=square()
s.typeshape()
s.rectangeShape()
s.squareShape()                                