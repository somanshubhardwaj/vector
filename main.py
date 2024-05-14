import math


class Vector:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y, self.z * other.z)

    def __truediv__(self, other):
        return Vector(self.x / other.x, self.y / other.y, self.z / other.z)

    def __str__(self):
        return f"Vector({self.x},{self.y},{self.z})"

    def scalar(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        return Vector(self.y * other.z - self.z * other.y, self.z * other.x - self.x * other.z,
                      self.x * other.y - self.y * other.x)

    def __repr__(self):
        return f"Vector({self.x},{self.y},{self.z})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y and self.z < other.z

    def __le__(self, other):
        return self.x <= other.x and self.y <= other.y and self.z <= other.z

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y and self.z > other.z

    def __ge__(self, other):
        return self.x >= other.x and self.y >= other.y and self.z >= other.z

    def __neg__(self):
        return Vector(-self.x, -self.y, -self.z)

    def __pos__(self):
        return Vector(+self.x, +self.y, +self.z)

    def __abs__(self):
        return Vector(abs(self.x), abs(self.y), abs(self.z))

    def __invert__(self):
        return Vector(~self.x, ~self.y, ~self.z)

    def __round__(self, n):
        return Vector(round(self.x, n), round(self.y, n), round(self.z, n))

    def __floor__(self):
        return Vector(math.floor(self.x), math.floor(self.y), math.floor(self.z))

    def __ceil__(self):
        return Vector(math.ceil(self.x), math.ceil(self.y), math.ceil(self.z))

    def __trunc__(self):
        return Vector(math.trunc(self.x), math.trunc(self.y), math.trunc(self.z))

    # Triple product
    def triple_product(self, other, another):
        return self.scalar(other.cross(another))

    # Scalar projection
    def scalar_projection(self, other):
        return self.scalar(other) / math.sqrt(other.scalar(other))

    # Vector projection
    def vector_projection(self, other):
        return other * (self.scalar(other) / other.scalar(other))

    # Angle between vectors
    def angle(self, other):
        return math.acos(self.scalar(other) / (math.sqrt(self.scalar(self)) * math.sqrt(other.scalar(other))))

    # Area of parallelogram
    def area_parallelogram(self, other):
        return self.cross(other).scalar(self.cross(other))

    # Area of triangle
    def area_triangle(self, other):
        return 0.5 * self.cross(other).scalar(self.cross(other))

    # Volume of parallelepiped
    def volume_parallelepiped(self, other, another):
        return self.scalar(other.cross(another))

    # Volume of tetrahedron
    def volume_tetrahedron(self, other, another):
        return abs(self.scalar(other.cross(another))) / 6

    # Distance between vectors
    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)

    # Midpoint of vectors
    def midpoint(self, other):
        return Vector((self.x + other.x) / 2, (self.y + other.y) / 2, (self.z + other.z) / 2)

    # Unit vector
    def unit_vector(self):
        return self / math.sqrt(self.scalar(self))

    # Perpendicular vector
    def perpendicular_vector(self):
        return Vector(-self.y, self.x, 0)

    # Projection of vector
    def projection(self):
        return self.scalar(self) / self.scalar(self)

    # Rotation of vector
    def rotation(self, angle):
        return Vector(self.x * math.cos(angle) - self.y * math.sin(angle),
                      self.x * math.sin(angle) + self.y * math.cos(angle), self.z)

    # Reflection of vector
    def reflection(self):
        return Vector(-self.x, -self.y, -self.z)

    # Vector components
    def components(self):
        return [self.x, self.y, self.z]

    # Vector magnitude
    def magnitude(self):
        return math.sqrt(self.scalar(self))

    # Vector direction
    def direction(self):
        return [self.x / self.magnitude(), self.y / self.magnitude(), self.z / self.magnitude()]

    # Vector normalization
    def normalize(self):
        return Vector(self.x / self.magnitude(), self.y / self.magnitude(), self.z / self.magnitude())
