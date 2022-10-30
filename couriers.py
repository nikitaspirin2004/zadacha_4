class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'Tочки с координатами {self.x}, {self.y}'
    def get_distance(self, other_point):
        x1 = self.x
        x2 = other_point.x
        y1 = self.y
        y2 = other_point.y
        dist = ((x2-x1)**2 + (y2-y1)**2)**0.5
        return dist
a = point(1,2)
b = point(3,5)
print (a.get_distance(b))