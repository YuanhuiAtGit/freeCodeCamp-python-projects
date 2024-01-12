class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
    
    def set_width(self, w):
        self.width = w
    
    def set_height(self, h):
        self.height = h

    def get_area(self):
        area = self.width * self.height
        return area
    
    def get_perimeter(self):
        peri = 2 * (self.width + self.height)
        return peri
    
    def get_diagonal(self):
        diagonal = (self.width ** 2 + self.height ** 2) ** .5
        return diagonal
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        each_row = "*"*self.width + "\n"
        row_lst = [each_row for _ in range(self.height)]
        picture = "".join(row_lst)
        return f"{picture}"
    
    def get_amount_inside(self, shape):
        div_by_width = self.width // shape.width
        div_by_height = self.height // shape.height
        return div_by_width*div_by_height
    

class Square(Rectangle):

    def __init__ (self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return f"Square(side={self.width})"

    def set_side(self, side):
        self.width = side
        self.height = side
    
    def set_width(self, w):
        self.set_side(w)

    def set_height(self, h):
        self.set_side(h)
    

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


    


            
            





