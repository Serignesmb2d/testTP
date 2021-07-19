from math import*

class Point():
    def __init__(self,a,b):
        self.x=a
        self.y=b

    def afficher(self):
        print(f"le coordonnes sont ( {self.x} , {self.y}) ")


class Cercle():
    def __init__(self, Point, rayon, couleur):
        self.centre = (Point.x, Point.y)
        self.__rayon = rayon
        self.couleur = couleur

    def getRayon(self):
        return self.__rayon

    def setRayon(self, val):
        self.__rayon = val

    def presenter(self):
        print (f"le cercle est de centre {self.centre}, de rayon {self.__rayon}, et de couleur {self.couleur}")

    def apartenir(self, Point):
        norm = sqrt(pow((Point.x - self.centre[0]),2) + pow((Point.y - self.centre[1]),2))

        if norm <= self.__rayon :
            print(f"le point est dans le cercle")

        else: 
            print("le point n appartient pas au cercle")

    def surface(self):
        sc = self.__rayon*self.__rayon*pi
        return(sc)

class Cylindre(Cercle):
    def __init__(self, Point, rayon, couleur, hauteur):
        super().__init__(Point, rayon, couleur)
        self.hauteur = hauteur

    def volume(self):
        v = super().surface() * self.hauteur 

        print("le volume est" , v)
p1 = Point(3,4)
c1 = Cercle(p1 , 4, "blanc")
cy = Cylindre(p1, 4, "blanc", 20)
cy.volume()
