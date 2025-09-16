import math
from symtable import Class
"""
********************
Class Point
********************
"""


class Point:
    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = x #appel le setter
        self.y = y #appel le setter

    #Property for x
    @property
    def x(self)->float:
        return self.__x

    @x.setter
    def x(self, x : float):
        self.__x = x

    #Property for y
    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, y: float):
        self.__y = y

    def __str__(self):
        return f"Point : ({self.__x}, {self.__y})"

    def distancecoordonnees(self, x:float, y:float)->float:
        d:float = math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)
        return d

    def distancePoint(self, p: "Point"):
        d:float=math.sqrt((self.__x-p.__x)*(self.__x-p.__x)+(self.__y-p.__y)*(self.__y-p.__y))
        return d

#Type d'utilisation
if __name__ == "__main__":
    p1 : Point = Point()
    p2 : Point = Point(3.5) #Appel des coordonnées de la classe Point
    print(p1)
    print(p2)
    print(f"distance :{p1.distancecoordonnees(2.2)}")
    print(f"distance :{p1.distancePoint(p2)}")

"""
********************
Class Cercle
********************
"""


class Cercle:
    def __init__(self, rayon : float, centre=None): #Ou centre = Point = None
        self.__rayon = rayon
        if centre is not None:
            self.__centre = centre
        else:
            self.__centre = Point(0.0, 0.0)

    def get_rayon(self):
        return self.__rayon

    # Setter pour le rayon
    def set_rayon(self, rayon: float):
        self.__rayon = rayon

    rayon = property(get_rayon, set_rayon) #méthode de suppression

    # Getter pour le centre
    def get_centre(self):
        return self.__centre

    # Setter pour le centre
    def set_centre(self, centre: Point):
        self.__centre = centre

    centre = property(get_centre, set_centre)

"""
********************
Class Rectangle
********************
"""

class Rectangle:
    def __init__(self, bas_gauche: Point = None, longueur: float = 1.0, hauteur: float = 1.0):
        self.__bas_gauche = bas_gauche if bas_gauche is not None else Point()
        self.__longueur = longueur
        self.__hauteur = hauteur

    @property
    def bas_gauche(self) -> Point:
        return self.__bas_gauche

    @bas_gauche.setter
    def bas_gauche(self, p: Point):
        self.__bas_gauche = p

    @property
    def longueur(self) -> float:
        return self.__longueur

    @longueur.setter
    def longueur(self, l: float):
        self.__longueur = l

    @property
    def hauteur(self) -> float:
        return self.__hauteur

    @hauteur.setter
    def hauteur(self, h: float):
        self.__hauteur = h

    def __str__(self):
        return f"Rectangle : Point bas-gauche {self.__bas_gauche}, longueur {self.__longueur}, hauteur {self.__hauteur}"

    def surface(self) -> float:
        return self.__longueur * self.__hauteur

    def perimetre(self) -> float:
        return 2 * (self.__longueur + self.__hauteur)

    def coin_haut_gauche(self) -> Point:
        return Point(self.__bas_gauche.x, self.__bas_gauche.y + self.__hauteur)

    def coin_haut_droit(self) -> Point:
        return Point(self.__bas_gauche.x + self.__longueur, self.__bas_gauche.y + self.__hauteur)

    def coin_bas_droit(self) -> Point:
        return Point(self.__bas_gauche.x + self.__longueur, self.__bas_gauche.y)

    def contient(self, p: Point) -> bool:
        return (self.__bas_gauche.x <= p.x <= self.__bas_gauche.x + self.__longueur and
                self.__bas_gauche.y <= p.y <= self.__bas_gauche.y + self.__hauteur)

#Type d'utilisation
if __name__ == "__main__":
    r = Rectangle(Point(1.0, 2.0), 4.0, 3.0)
    print(r)
    print("Surface :", r.surface())
    print("Périmètre :", r.perimetre())
    print("Coin haut gauche :", r.coin_haut_gauche())
    print("Point (2,3) dans le rectangle ?", r.contient(Point(2.0, 3.0)))
