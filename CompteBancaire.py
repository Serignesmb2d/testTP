class CompteBancaire :
    def __init__(self, nomCompte, numeroCompte, solde):

        self.numeroCompte= numeroCompte
        self.nomCompte= nomCompte
        self.solde=solde
        
    def versement(self,argent):
        self.solde+=argent
        print(argent)

        #print(self.solde)

    def retrait(self,argent):
        if self.solde<argent :
            print("Solde insuffisant")
        else:
            self.solde-=argent

    def Agios(self):
        agios= self.solde*0.05
        self.solde = self.solde-agios
        return self.solde
        

    def affichage(self):
        print(f"le numero de compte {self.numeroCompte} de nom {self.nomCompte} contient {self.solde} CFA")

c1 = CompteBancaire("diop",12,12000) 
c1.versement(20000)
c1.affichage()

