class Banana:
    def __init__(self,weight):
        self.color = 'yellow'
        self.weight = weight
    def __cmp__(self, other):
        return self.weight == other.weight
b1 = Banana(12)
b2 = Banana(12)
print (b1 == b2)