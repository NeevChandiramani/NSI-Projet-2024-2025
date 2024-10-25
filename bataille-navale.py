class Joueur:
    def __init__(self, nom, numero):
        self.nom = nom
        self.numero = numero

    def Joueur1(self):
        self.numero = 1
        self.nom = "Joueur 1"
        return self.nom

    def Joueur2(self):
        self.numero = 2
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

    def boulet_de_canon(self):
        if self.numero == 1 :
            tire_ligne = input() #max doit la finir
        

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

    def placer_bateau(self):
        for i in ListeBateaux :
            print(f"Le nom du bateau est {self.nom}, ça longueur est de {self.longueur}")
            placementLigne = input("Où voulez-vous placer le bateau sur la ligne ? Choisissez un nombre entre 1 et 10 inclues.")
            placementColonne = input("Où voulez-vous placer le bateau sur la colonne ? Choisissez une lettre entre A et J inclues.")
            rep = input("Notez bien que le bateau sera affiché en LONGUEUR à partir du point choisi, si vous voulez faire une rotation du bateau, écrivez 'oui' ")          
            if rep == "oui" :
                self.bateau.rotate
            else :
                None
            
            #je suis perdu à partie d'ici
            #for i in self.grille[placementColonne] :
                #print('X')

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
ListeBateaux = [
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



'_________________________________________________________________________________________________'

#Exemple 1 avec un dico

dictionnaire_grille = { 'A' : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                        'B' : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                        'C' : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                        'D' : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                        'E' : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                        'F' : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                        'G' : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                        'H' : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                        'I' : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                        'J' : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] }

#print(dictionnaire_grille['A'])

def créer_grille(dictionnaire_grille) :
    print("  1 2 3 4 5 6 7 8 9 10")
    for i in dictionnaire_grille.keys :
        print(i, end = ' ')
        print(dictionnaire_grille[i])


def créer_grille(dictionnaire_grille) :
    print("   1  2  3  4  5  6  7  8  9  10")
    for i in dictionnaire_grille :
        print(i, end = ' ')
        print(dictionnaire_grille[i])

#créer_grille(dictionnaire_grille)
