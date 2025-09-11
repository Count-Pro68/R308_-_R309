import math

class Point:
    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = x
        self.y = y

    def __str__(self):
        return (f"Point : ({self.__x}, {self.__y}")

    def distancecoordonnees(self, x:float, y:float)->float:
        d:float = math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)
        return d

    def distancePoint(self, p: Point):
        d:float=math.sqrt((self.__x-p.__x)*(self.__x-p.__x)+(self.__y-p.__y)*(self.__y-p.__y))
        return d



if __name__ = "__main__":
    p1 : Point = Point()
    p2 : Point = Point(3.5)
    print(p1)
    print(p2)
    print(f"distance :{p1.distancecoordonnees(2.2)}")
    print(f"distance :{p1.distancePoint(p2)}")
