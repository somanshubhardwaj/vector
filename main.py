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
    
if __name__ == "__main__":
    v1 = Vector(1,2,3)
    v2 = Vector(4,5,6)
    print(v1+v2)
    print(v1-v2)
    print(v1*v2)
    print(v1/v2)
    print(v1.scalar(v2))
    print(v1.cross(v2))        