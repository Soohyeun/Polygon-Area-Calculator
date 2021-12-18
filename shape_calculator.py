class Rectangle:

# set width and height when object is created
    def __init__ (self, width, height):
        self.width = width
        self.height = height

# when instance is represented, it returns
    def __str__(self):
        return 'Rectangle(width=%d, height=%d)'%(self.width, self.height)

# change the width
    def set_width(self, width):
        self.width = width

#change the height
    def set_height(self, height):
        self.height = height

#calculate area
    def get_area(self):
        self.area = self.width * self.height
        return self.area

#calculate perimeter
    def get_perimeter(self):
        self.perimeter = 2*self.width + 2*self.height
        return self.perimeter

#calculate diagonal length
    def get_diagonal(self):
        self.diagonal = (self.width**2 + self.height**2)**0.5
        return self.diagonal

#draw the rectangle with *
    def get_picture(self):
        self.s = ''
        if self.width <= 50 and self.height <= 50:
            for i in range(self.height):
                self.s = self.s + '*'*self.width + '\n'
            return self.s
        else:
            return 'Too big for picture.'


    def get_amount_inside(self, other):
        self.x = self.width // other.width
        self.y = self.height // other.height
        return self.x*self.y


class Square(Rectangle):

# store attributes from the Rectangle class
    def __init__(self, side):
        super().__init__(side,side)

    def __str__ (self):
        return 'Square(side=%d)'%self.width

#set both the width and height
    def set_side(self, side):
        self.height = side
        self.width = side

    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(side)


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
