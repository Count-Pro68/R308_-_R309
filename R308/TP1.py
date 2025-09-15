import math
from symtable import Class


class Point:
    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = x
        self.y = y

    @property
    def x(self)->float:
        return self.__x
    @x.setter
    def x(self, x : float):
        self.__x=x

    def __str__(self):
        return (f"Point : ({self.__x}, {self.__y}")

    def distancecoordonnees(self, x:float, y:float)->float:
        d:float = math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)
        return d

    def distancePoint(self, p: "Point"):
        d:float=math.sqrt((self.__x-p.__x)*(self.__x-p.__x)+(self.__y-p.__y)*(self.__y-p.__y))
        return d

if __name__ == "__main__":
    p1 : Point = Point()
    p2 : Point = Point(3.5) #Appel des coordonnées de la classe Point
    print(p1)
    print(p2)
    print(f"distance :{p1.distancecoordonnees(2.2)}")
    print(f"distance :{p1.distancePoint(p2)}")

"""
********************
Changement de class
********************
"""


class Cercle:
    def __init__(self, rayon : float, centre : Point = 0.0 = none):
        self.__rayon = rayon
        if centre is not none:
            self.__centre = centre
        else :
            self.__centre = Point(0.0)