import math

class Vector:
    def __init__(self, name, x, y, z):
        self.name, self.x, self.y, self.z = name, x, y, z

    def norm(self):
        n = math.sqrt(self.x**2 + self.y**2 + self.z**2)
        print(f"{self.name} = {n}")
        return n
        
vectorA = Vector('A', 2, 3, 4)
vectorB = Vector('B', 5, 6, 7)
vectorA.norm()
vectorB.norm()

class Scalar(Vector):
    def __init__(self, name, x, y, z):
        super().__init__(name, x, y, z)
    
    def scalarproduct(obj1, obj2):
        c = obj1.x * obj2.x + obj1.y * obj2.y + obj1.z * obj2.z
        print(f"{c} e skalarno proizvedenie")
        return c

    def cosalpha(a, b, c):
        cos = c / (a * b)
        degrees = 180 * cos / math.pi
        print(f"cosalpha e {degrees:.1f} degrees")
        return degrees

    def proverka(degrees, a, b):
        cos = (math.pi * degrees) / 180
        ab = a * b * cos
        print(ab)
        return ab

scalarA = Scalar("A", 2, 3, 4)
scalarB = Scalar("B", 5, 6, 7)
a = scalarA.norm()
b = scalarB.norm()
c = Scalar.scalarproduct(scalarA, scalarB)
cos = Scalar.cosalpha(a, b, c)
Scalar.proverka(cos, a, b)
