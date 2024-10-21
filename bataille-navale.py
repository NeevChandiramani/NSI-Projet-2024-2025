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

    def affiche_nom(self):
        print("Votre pseudo est : ", self.nom)
        return self.nom
    

class Bateau:
    def __init__(self, nom, longueur, vie, largeur=1):
        self.nom = nom
        self.longueur = longueur
        self.largeur = largeur
        self.vie = vie
        
    def rotate(self):
        # Permet de changer l'orientation du bateau (horizontal à vertical)
        self.longueur, self.largeur = self.largeur, self.longueur
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

    def boulet_de_canon():
        #permet de lancer un boulet sur la grille de défense de l'adversaire
        pass
    
    def affiche_boulet():
        #permet d'affiche le boulet de canon sur la grille d'attaque du joueur pour savoir s'il a touché ou non
        pass
    
    


class Grille_Défense: # celle ou on place nos bateaux
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

    def placer_bateau():
        #placer les bateaux sur la grille déf au début de la partie
        pass

    def affiche_bateau():
        #affiche la grille avec les bateaux,
        #les bateaux sont marqués avec une succession de "X"
        pass
    
    def affiche_toucher():
        #affiche sur le grille defense si l'un de ses bateux c'est fait hit et le supprime si il n'a plus de vie et si c'etait son dernier bateau ecrit victoire 
        pass

    
    

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


    def verifier_victoire():
        pass



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


