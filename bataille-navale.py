class Joueur:
    # définition de la classe Joueur qui représente un joueur du jeu

    def __init__(self, nom, numero):
        # constructeur de la classe Joueur qui initialise le nom et le numéro du joueur
        self.nom = nom  # nom du joueur
        self.numero = numero  # numéro du joueur pour l'identifier  (1 ou 2)

    def Joueur1(self):
        # méthode pour configurer le joueu comme "Joueur 1"
        self.numero = 1  # attribue le numéro 1
        self.nom = "Joueur 1"  # définit le nom par défaut pour le joueur 1
        return self.nom  # retourne le nom du joueur

    def Joueur2(self):
        # méthode pour configurer le joueur comme "Joueur 2"
        self.numero = 2  # attribue le numéro 2
        self.nom = "Joueur 2"  # définit le nom par défaut pour le joueur 2
        return self.nom  # retourne le nom du joueur

    def choix_nom(self):
        # méthode pour permettre au joueur de choisir un pseudonyme
        self.nom = input("Quel pseudo voulez-vous choisir ? ")  # demande à l utilisateur d'entrer un pseudo
        return self.nom  # retourne le pseudo choisi

    def affiche_nom(self):
        # méthode pour afficher le nom actuel du joueur
        print("Votre pseudo est :", self.nom)  # affiche le pseudo du joueur
        return self.nom  # retourne le nom du joueur




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
    def __init__(self, joueur, bateau, grille):
        self.joueur = joueur
        self.bateau = bateau
        self.grille = grille


    def créer_grille(self, dictionnaire_grille) :
        for i in dictionnaire_grille :
            dictionnaire_grille[i] = ['~'] * 10


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
    def __init__(self, joueur, bateau, grille):
        self.joueur = joueur
        self.bateau = bateau
        self.grille = grille
    
    def créer_grille(dictionnaire_grille) :
        for i in dictionnaire_grille :
            dictionnaire_grille[i] =['~'] * 10

    

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

    def verifier_victoire(self,):
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



def affiche_grille(dictionnaire_grille) :
    print("   1  2  3  4  5  6  7  8  9  10")
    for i in dictionnaire_grille :
        print(i, end = ' ')
        print(dictionnaire_grille[i])

#créer_grille(dictionnaire_grille)
############################################################################################################################################################################################################################################################################################################################################################
import os
import time

class Bateau:
    def __init__(self, nom, taille):
        self.nom = nom
        self.taille = taille
        self.positions = []
        self.touches = []
    
    def est_coule(self):
        """Vérifie si le bateau est coulé"""
        return len(self.touches) == self.taille
    
    def est_touche(self, x, y):
        """Vérifie si une position donnée touche le bateau"""
        return (x, y) in self.positions

class Plateau:
    def __init__(self, nom_joueur, taille=10):
        self.nom_joueur = nom_joueur
        self.taille = taille
        self.grille = [['~' for _ in range(taille)] for _ in range(taille)]
        self.bateaux = []
        
        # Symboles pour l'affichage
        self.EAU = '~'
        self.BATEAU = 'B'
        self.TOUCHE = 'X'
        self.RATE = 'O'
    
    def afficher(self, montrer_bateaux=False):
        """Affiche le plateau de jeu"""
        print(f"\nPlateau de {self.nom_joueur}:")
        print("  ", end="")
        for i in range(self.taille):
            print(f"{i} ", end="")
        print("\n")
        
        for i in range(self.taille):
            print(f"{i} ", end="")
            for j in range(self.taille):
                symbole = self.grille[i][j]
                if not montrer_bateaux and symbole == self.BATEAU:
                    print(f"{self.EAU} ", end="")
                else:
                    print(f"{symbole} ", end="")
            print()
    
    def placer_bateau(self, bateau, x, y, horizontal):
        """Place un bateau sur le plateau"""
        positions_possibles = []
        
        if horizontal:
            if y + bateau.taille > self.taille:
                return False
            
            for i in range(bateau.taille):
                if self.grille[x][y + i] != self.EAU:
                    return False
                positions_possibles.append((x, y + i))
        else:
            if x + bateau.taille > self.taille:
                return False
            
            for i in range(bateau.taille):
                if self.grille[x + i][y] != self.EAU:
                    return False
                positions_possibles.append((x + i, y))
        
        for pos_x, pos_y in positions_possibles:
            self.grille[pos_x][pos_y] = self.BATEAU
        
        bateau.positions = positions_possibles
        self.bateaux.append(bateau)
        return True
    
    def recevoir_tir(self, x, y):
        """Traite un tir reçu"""
        if not (0 <= x < self.taille and 0 <= y < self.taille):
            return False, "Tir hors du plateau !"
        
        if self.grille[x][y] in [self.TOUCHE, self.RATE]:
            return False, "Cette case a déjà été touchée !"
        
        for bateau in self.bateaux:
            if (x, y) in bateau.positions:
                bateau.touches.append((x, y))
                self.grille[x][y] = self.TOUCHE
                
                if bateau.est_coule():
                    return True, f"Coulé ! Le {bateau.nom} est détruit !"
                return True, "Touché !"
        
        self.grille[x][y] = self.RATE
        return True, "Manqué !"

class BatailleNavaleMultijoueur:
    def __init__(self):
        # Demande les noms des joueurs
        print("=== BATAILLE NAVALE MULTIJOUEUR ===")
        self.nom_joueur1 = input("Nom du Joueur 1: ")
        self.nom_joueur2 = input("Nom du Joueur 2: ")
        
        # Crée les plateaux
        self.plateau_joueur1 = Plateau(self.nom_joueur1)
        self.plateau_joueur2 = Plateau(self.nom_joueur2)
        
        # Définition des bateaux
        self.types_bateaux = [
            ("Porte-avions", 5),
            ("Croiseur", 4),
            ("Contre-torpilleur", 3),
            ("Sous-marin", 3),
            ("Torpilleur", 2)
        ]

    def effacer_ecran(self):
        """Efface l'écran pour plus de confidentialité"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def attendre_joueur(self, nom_joueur):
        """Attend que le joueur soit prêt"""
        input(f"\n{nom_joueur}, appuyez sur Entrée quand vous êtes prêt...")
        self.effacer_ecran()
    
    def placer_bateaux_joueur(self, plateau, nom_joueur):
        """Permet à un joueur de placer ses bateaux"""
        print(f"\n{nom_joueur}, placez vos bateaux:")
        
        for nom, taille in self.types_bateaux:
            while True:
                plateau.afficher(True)
                print(f"\nPlacer le {nom} (taille: {taille})")
                
                try:
                    x = int(input("Ligne (0-9): "))
                    y = int(input("Colonne (0-9): "))
                    orientation = input("Horizontal (o/n)? ").lower()
                    horizontal = orientation == 'o'
                    
                    if plateau.placer_bateau(Bateau(nom, taille), x, y, horizontal):
                        break
                    else:
                        print("\nPosition invalide ! Réessayez.")
                except ValueError:
                    print("\nEntrée invalide ! Utilisez des nombres entre 0-9.")
    
    def tour_joueur(self, attaquant, defenseur, nom_attaquant, nom_defenseur):
        """Gère le tour d'un joueur"""
        print(f"\nTour de {nom_attaquant}:")
        print("\nVotre plateau:")
        attaquant.afficher(True)
        print("\nPlateau adverse:")
        defenseur.afficher(False)
        
        while True:
            try:
                x = int(input("Ligne de tir (0-9): "))
                y = int(input("Colonne de tir (0-9): "))
                
                valide, message = defenseur.recevoir_tir(x, y)
                print(message)
                
                if valide:
                    return self.verifier_victoire(defenseur)
            except ValueError:
                print("Entrée invalide ! Utilisez des nombres entre 0-9.")
    
    def verifier_victoire(self, plateau):
        """Vérifie si tous les bateaux sont coulés"""
        return all(bateau.est_coule() for bateau in plateau.bateaux)
    
    def jouer(self):
        """Lance une partie"""
        # Phase de placement des bateaux
        self.placer_bateaux_joueur(self.plateau_joueur1, self.nom_joueur1)
        self.attendre_joueur(self.nom_joueur2)
        
        self.placer_bateaux_joueur(self.plateau_joueur2, self.nom_joueur2)
        self.attendre_joueur(self.nom_joueur1)
        
        # Boucle de jeu
        tour_joueur1 = True
        
        while True:
            self.effacer_ecran()
            
            if tour_joueur1:
                if self.tour_joueur(self.plateau_joueur1, self.plateau_joueur2, 
                                  self.nom_joueur1, self.nom_joueur2):
                    print(f"\nFélicitations {self.nom_joueur1} ! Vous avez gagné !")
                    break
            else:
                if self.tour_joueur(self.plateau_joueur2, self.plateau_joueur1,
                                  self.nom_joueur2, self.nom_joueur1):
                    print(f"\nFélicitations {self.nom_joueur2} ! Vous avez gagné !")
                    break
            
            tour_joueur1 = not tour_joueur1
            self.attendre_joueur(self.nom_joueur1 if tour_joueur1 else self.nom_joueur2)

# Lancement du jeu
if __name__ == "__main__":
    jeu = BatailleNavaleMultijoueur()
    jeu.jouer()