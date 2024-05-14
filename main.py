import math
class Vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self,other):
        return Vector(self.x+other.x,self.y+other.y,self.z+other.z)
    def __sub__(self,other):
        return Vector(self.x-other.x,self.y-other.y,self.z-other.z)
    def __mul__(self,other):
        return Vector(self.x*other.x,self.y*other.y,self.z*other.z)
    def __truediv__(self,other):
        return Vector(self.x/other.x,self.y/other.y,self.z/other.z)
    def __str__(self):
        return f"Vector({self.x},{self.y},{self.z})"
    def scalar(self,other):
        return self.x*other.x+self.y*other.y+self.z*other.z
    def cross(self,other):
        return Vector(self.y*other.z-self.z*other.y,self.z*other.x-self.x*other.z,self.x*other.y-self.y*other.x)
    def __repr__(self):
        return f"Vector({self.x},{self.y},{self.z})"
    def __eq__(self,other):
        return self.x == other.x and self.y == other.y and self.z == other.z
    def __ne__(self,other):
        return not self.__eq__(other)
    def __lt__(self,other):
        return self.x < other.x and self.y < other.y and self.z < other.z
    def __le__(self,other):
        return self.x <= other.x and self.y <= other.y and self.z <= other.z
    def __gt__(self,other):
        return self.x > other.x and self.y > other.y and self.z > other.z
    def __ge__(self,other):
        return self.x >= other.x and self.y >= other.y and self.z >= other.z
    def __neg__(self):
        return Vector(-self.x,-self.y,-self.z)
    def __pos__(self):
        return Vector(+self.x,+self.y,+self.z)
    def __abs__(self):
        return Vector(abs(self.x),abs(self.y),abs(self.z))
    def __invert__(self):
        return Vector(~self.x,~self.y,~self.z)
    def __round__(self,n):
        return Vector(round(self.x,n),round(self.y,n),round(self.z,n))
    def __floor__(self):
        return Vector(math.floor(self.x),math.floor(self.y),math.floor(self.z))
    def __ceil__(self):
        return Vector(math.ceil(self.x),math.ceil(self.y),math.ceil(self.z))
    def __trunc__(self):
        return Vector(math.trunc(self.x),math.trunc(self.y),math.trunc(self.z))

 