class Rectangle():
    def __init__(self, longueur, largeur):
        self.longueur=longueur
        self.largeur=largeur
    
    def perimetre(self):

        p= (self.longueur+self.largeur)*2

        print(p)

    def surface(self):
        s=(self.longueur*self.largeur)
        print(s)

    def get_longueur(self):
        return self.longueur

    def get_largeur(self):
        return self.largeur

    def set_longueur(self):
        return self.longueur

    
    def set_largeur(self):
        return self.largeur

class Parapipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        Rectangle.__init__(self, longueur, largeur)
        self.hauteur = hauteur

    def volume(self):
        v = self.longueur*self.largeur*self.hauteur
        print(v)

rect =Rectangle(4,5)
rect.perimetre()
rect.surface()
para =Parapipede(4, 2, 2)
para.volume()