# define class name Shape

class Shape():
    
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __area(self):
        return self.width * self.height

    def __Scope(self):
        return 2*self.width+2*self.height

    def get_width(self):
        return self.width

    def set_width(self, width):
        self.width = width

    def get_height(self):
        return self.height


    def set_height(self, height):
        self.height = height


    def __str__(self):
        return f'{self.width} {self.height}'

    def __repr__(self):
        rep='shape('+str(self.width)+','+str(self.height)+')'
        return rep
        
