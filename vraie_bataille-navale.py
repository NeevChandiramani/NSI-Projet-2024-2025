import random

class Bateau:
    def __init__(self, nom, taille):
        self.nom = nom        # Nom du bateau (ex: "Porte-avions")
        self.taille = taille  # Longueur du bateau
        self.positions = []   # Liste des coordonnées occupées par le bateau
        self.touches = []     # Liste des positions touchées par l'adversaire
    
    
    def est_coule(self):
        """Vérifie si le bateau est coulé (toutes les positions sont touchées)"""
        return len(self.touches) == self.taille
    
    def est_touche(self, x, y):
        """Vérifie si une position donnée touche le bateau"""
        return (x, y) in self.positions
    


class Plateau:
    def __init__(self, taille=10):
        # Création du plateau vide (eau partout)
        self.taille = taille
        self.grille = []
        for _ in range(taille):
            ligne = ['~'] * taille
            self.grille.append(ligne)
        self.bateaux = []
        
        # Symboles utilisés pour l'affichage
        self.EAU = '~'        # Case d'eau
        self.BATEAU = 'B'     # Case avec un bateau
        self.TOUCHE = 'X'     # Tir qui a touché
        self.RATE = 'O'       # Tir raté

    def afficher(self, montrer_bateaux = False) :
        print ("   1 2 3 4 5 6 7 8 9")
        for i in range(self.taille) :
            print(i, end = ' ')
            for j in range(self.taille) :
                print(self.EAU, end = ' ')
            print()


    def placer_bateau():
        
        pass

    
    def boulet_de_canon(self, x, y) :
        if not (0 <= x < self.taille and 0 <= y < self.taille) :    #Définir si le boulet est dans la grille
            print ("Le boulet de canon est sorti de la grille")
            return False
        if self.grille[x][y] == self.TOUCHE or self.grille[x][y] == self.RATE :     #Définir si l'endroit de la grille n'a pas déjà été touché.
            print ("Un boulet de canon a déjà atterit ici !")
            return False
        for bateau in self.bateaux :
            if (x, y) in bateau.positions :
                bateau.touches.append((x, y))
                self.grille[x][y] = self.TOUCHE
                if bateau.est_coule() :
                    print (f" Touché Coulé, le {bateau.nom} est détruit !")
                    return True
                else :
                    print ("Touché !")
                    return True
            else :
                self.grille[x][y] = self.RATE
                print ("Manqué !")
                return True
