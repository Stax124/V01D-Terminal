class Vector3():
    def __init__(self,x:float,y:float,z:float):
        self.x = x
        self.y = y
        self.z = z
        self.value = self.x,self.y,self.z
        self.magnitude = pow(pow(self.x,2)+pow(self.y,2)+pow(self.z,2),0.5)
    def __add__(self,other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
    def __sub__(self,other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
    def __mul__(self,other):
        return Vector3(self.x * other.x, self.y * other.y, self.z * other.z)
    def __truediv__(self,other):
        return Vector3(self.x / other.x, self.y / other.y, self.z / other.z)
    def __repr__(self):
        return repr((self.x, self.y,self.z))
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y and self.z == other.z:
            return True
        else: return False
    def normalize(self):
        return self.x / self.magnitude, self.y / self.magnitude, self.z / self.magnitude

class Vector2():
    def __init__(self,x:float,y:float):
        self.x = x
        self.y = y
        self.value = self.x,self.y
        self.magnitude = pow(pow(self.x,2)+pow(self.y,2),0.5)
    def __add__(self,other):
        return Vector2(self.x + other.x, self.y + other.y)
    def __sub__(self,other):
        return Vector2(self.x - other.x, self.y - other.y)
    def __mul__(self,other):
        return Vector2(self.x * other.x, self.y * other.y)
    def __truediv__(self,other):
        return Vector2(self.x / other.x, self.y / other.y)
    def __repr__(self):
        return repr((self.x, self.y))
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else: return False
    def normalize(self):
        return Vector2(self.x / self.magnitude, self.y / self.magnitude)