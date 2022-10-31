class Point:
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
class Couriers:
    def __init__(self, x, y):
        self.x = x
        self.y = y

'''заказы'''
z1 = Point(1,2)
z2 = Point(3,4)
z3 = Point(3,1)
z4 = Point(3,7)
z5 = Point (4,1)
'''курьеры'''
k1 = Couriers(3,2)
k2 = Couriers(1,1)
k3 = Couriers(2,4)
k4 = Couriers(3,6)
k5 = Couriers(1,5)
zakazi = [z1,z2,z3,z4,z5]
kurieri = [k1,k2,k3,k4,k5]
for i in range (5):
    kz = []
    for k in range (5):
        kz.append(zakazi[i].get_distance(kurieri[k]))
    coirier = kz.index(min(kz))
    min_distance = min(kz)
    for k in range(5):
        if min_distance == zakazi[i].get_distance(kurieri[k]):
            kurieri[k].x = zakazi[i].x
            kurieri[k].y = zakazi[i].y

    print('Заказ №', i + 1, 'заберет', coirier + 1, "курьер.")