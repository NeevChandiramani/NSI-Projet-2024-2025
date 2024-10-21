class Joueur:
    def __init__(self, nom):
        self.nom = nom

    def Joueur1(self):
        self.nom = "Joueur 1"
        return self.nom

    def Joueur2(self):
        self.nom = "Joueur 2"
        return self.nom

    def choix_nom(self):
        self.nom = input("Quel pseudo voulez-vous choisir ? ")
        return self.nom

class Bateau:
    def __init__(self, longueur, largeur=1, vie, nom):
        self.longueur = longueur
        self.vie = vie
        self.nom = nom
        self.largeur = largeur

    def rotate(self) :
        a = self.longueur
        self.longueur = self.largeur
        self.largeur = a
        ## A finir après avoir fait la classe Jeu

class Grille_Attaque:
    def __init__(self, joueur, bateau):
        self.joueur = joueur
        self.bateau = bateau
        self.grille = {lettre: ['~' for _ in range(10)] for lettre in 'ABCDEFGHIJ'}

    def afficher_grille(self):
        print("  1 2 3 4 5 6 7 8 9 10")
        for lettre in 'ABCDEFGHIJ':
            print(lettre, end=' ')
            for case in self.grille[lettre]:
                print(case, end=' ')
            print()


class Grille_Défense:
    def __init__(self, joueur, bateau):
        self.joueur = joueur
        self.bateau = bateau
        self.grille = {lettre: ['~' for _ in range(10)] for lettre in 'ABCDEFGHIJ'}

    def afficher_grille(self):
        print("  1 2 3 4 5 6 7 8 9 10")
        for lettre in 'ABCDEFGHIJ':
            print(lettre, end=' ')
            for case in self.grille[lettre]:
                print(case, end=' ')
            print()

#    def test_afficher_grille(self):
#        for i, lettre in enumerate('ABCDEFGHIJ'):
#            self.grille[lettre][i] = 'X'
#        self.afficher_grille()


class Jeu:
    def __init__(self, Joueur1, Joueur2, Grille_Attaque, Grille_Défense, Bateau):
        self.Joueur1 = Joueur1
        self.Joueur2 = Joueur2
        self.Grille_Attaque = Grille_Attaque
        self.Grille_Défense = Grille_Défense
        self.Bateau = Bateau

    








# Création des bateaux
bateaux = [
    Bateau(5, 5, "Le Charles de Gaulle"),
    Bateau(4, 4, "Le mistral"),
    Bateau(3, 3, "L'Aquitaine"),
    Bateau(3, 3, "La Fayette"),
    Bateau(2, 2, "Le Laffaux"),
    Bateau(1,1, "La Barque")
]

# Test de la classe Grilles
#if __name__ == "__main__":
#    joueur = Joueur("Joueur 1")
#    grille = Grilles(joueur, bateaux[0])  # Using the first boat for this example
#    print("Test de la fonction afficher_grille")
#    grille.test_afficher_grille()


