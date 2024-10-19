class Joueur :
    def __init__ (self, nom) :
        self.nom = nom

    def choix_nom (self) :
        self.nom = input("Quel pseudo voulez-vous choisir ?")
        return    
        

class Bateau :
    def __init__ (self, L, l, vie) :
        self.longueur = L
        self.largeur = l
        self.vie = vie


#bateaux à définir


class Grille_def :
    def __init__ (self, x, y) :
        self.abscisse = x
        self.ordonnee = y


class Grille_atk :
    def __init__ (self, x, y) :
        self.abscisse = x
        self.ordonnee = y
