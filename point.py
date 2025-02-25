class Point (object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f'<{self.x},{self.y}>'
    def __add__(self,other):
        return Point(self.x + other.x,self.y + other.y)
    def __sub__(self,other):
            return Point(self.x - other.x,self.y - other.y)
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False