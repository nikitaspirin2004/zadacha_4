class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'Tочки с координатами {self.x}, {self.y}'
p1 = point(1,2)
print(p1)
