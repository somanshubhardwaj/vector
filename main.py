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
    """
    A class to represent a 3-dimensional vector and perform vector operations.

    Attributes:
    x (float): The x-coordinate of the vector.
    y (float): The y-coordinate of the vector.
    z (float): The z-coordinate of the vector.

    Methods:
    __init__(self, x, y, z):
        Initializes a Vector object with the given x, y, and z coordinates.
    __add__(self, other):
        Adds two vectors element-wise and returns the resulting vector.
    __sub__(self, other):
        Subtracts one vector from another element-wise and returns the resulting vector.
    __mul__(self, other):
        Multiplies two vectors element-wise and returns the resulting vector.
    __truediv__(self, other):
        Divides one vector by another element-wise and returns the resulting vector.
    __str__(self):
        Returns a string representation of the vector in the format "Vector(x, y, z)".
    scalar(self, other):
        Computes the scalar (dot) product of two vectors and returns the result.
    cross(self, other):
        Computes the cross product of two vectors and returns the resulting vector.
    __repr__(self):
        Returns a string representation of the vector suitable for reproduction of the object.
    __eq__(self, other):
        Checks if two vectors are equal.
    __ne__(self, other):
        Checks if two vectors are not equal.
    __lt__(self, other):
        Checks if all components of self are less than corresponding components of other.
    __le__(self, other):
        Checks if all components of self are less than or equal to corresponding components of other.
    __gt__(self, other):
        Checks if all components of self are greater than corresponding components of other.
    __ge__(self, other):
        Checks if all components of self are greater than or equal to corresponding components of other.
    __neg__(self):
        Returns the negation of the vector.
    __pos__(self):
        Returns the vector unchanged.
    __abs__(self):
        Returns a vector with the absolute values of each component.
    __invert__(self):
        Returns a vector with bitwise inversion of each component.
    __round__(self, n):
        Returns a vector with each component rounded to the nearest multiple of 10**(-n).
    __floor__(self):
        Returns a vector with each component rounded down to the nearest integer.
    __ceil__(self):
        Returns a vector with each component rounded up to the nearest integer.
    __trunc__(self):
        Returns a vector with each component truncated to the nearest integer towards zero.
    """


 