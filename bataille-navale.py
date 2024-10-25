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
        self.grille = [['~' for _ in range(taille)] for _ in range(taille)]
        self.bateaux = []
        
        # Symboles utilisés pour l'affichage
        self.EAU = '~'        # Case d'eau
        self.BATEAU = 'B'     # Case avec un bateau
        self.TOUCHE = 'X'     # Tir qui a touché
        self.RATE = 'O'       # Tir raté
    
    def afficher(self, montrer_bateaux=False):
        """Affiche le plateau de jeu"""
        # Affichage des numéros de colonnes
        print("\n  ", end="")
        for i in range(self.taille):
            print(f"{i} ", end="")
        print("\n")
        
        # Affichage des lignes
        for i in range(self.taille):
            print(f"{i} ", end="")  # Numéro de ligne
            for j in range(self.taille):
                symbole = self.grille[i][j]
                # Cache les bateaux si demandé
                if not montrer_bateaux and symbole == self.BATEAU:
                    print(f"{self.EAU} ", end="")
                else:
                    print(f"{symbole} ", end="")
            print()  # Nouvelle ligne
    
    def placer_bateau(self, bateau, x, y, horizontal):
        """Essaie de placer un bateau aux coordonnées données"""
        positions_possibles = []
        
        # Vérifie si le bateau peut être placé horizontalement
        if horizontal:
            # Vérifie si le bateau ne sort pas du plateau
            if y + bateau.taille > self.taille:
                return False
            
            # Vérifie si les cases sont libres
            for i in range(bateau.taille):
                if self.grille[x][y + i] != self.EAU:
                    return False
                positions_possibles.append((x, y + i))
        
        # Placement vertical
        else:
            # Vérifie si le bateau ne sort pas du plateau
            if x + bateau.taille > self.taille:
                return False
            
            # Vérifie si les cases sont libres
            for i in range(bateau.taille):
                if self.grille[x + i][y] != self.EAU:
                    return False
                positions_possibles.append((x + i, y))
        
        # Place le bateau sur le plateau
        for pos_x, pos_y in positions_possibles:
            self.grille[pos_x][pos_y] = self.BATEAU
        
        # Enregistre les positions dans le bateau
        bateau.positions = positions_possibles
        self.bateaux.append(bateau)
        return True
    
    def recevoir_tir(self, x, y):
        """Traite un tir aux coordonnées données"""
        # Vérifie si les coordonnées sont valides
        if not (0 <= x < self.taille and 0 <= y < self.taille):
            return False, "Tir hors du plateau !"
        
        # Vérifie si la case a déjà été touchée
        if self.grille[x][y] in [self.TOUCHE, self.RATE]:
            return False, "Cette case a déjà été touchée !"
        
        # Cherche si un bateau est touché
        for bateau in self.bateaux:
            if (x, y) in bateau.positions:
                bateau.touches.append((x, y))
                self.grille[x][y] = self.TOUCHE
                
                if bateau.est_coule():
                    return True, f"Coulé ! Le {bateau.nom} est détruit !"
                return True, "Touché !"
        
        # Aucun bateau touché
        self.grille[x][y] = self.RATE
        return True, "Manqué !"

class BatailleNavale:
    def __init__(self):
        self.plateau_joueur = Plateau()
        self.plateau_ordinateur = Plateau()
        
        # Définition des bateaux du jeu
        self.types_bateaux = [
            ("Porte-avions", 5),
            ("Croiseur", 4),
            ("Contre-torpilleur", 3),
            ("Sous-marin", 3),
            ("Torpilleur", 2)
        ]
    
    def placer_bateaux_joueur(self):
        """Permet au joueur de placer ses bateaux"""
        print("\nPlacement de vos bateaux:")
        for nom, taille in self.types_bateaux:
            while True:
                self.plateau_joueur.afficher(True)
                print(f"\nPlacer le {nom} (taille: {taille})")
                
                try:
                    # Demande les coordonnées
                    x = int(input("Ligne (0-9): "))
                    y = int(input("Colonne (0-9): "))
                    
                    # Demande l'orientation
                    orientation = input("Horizontal (o/n)? ").lower()
                    horizontal = orientation == 'o'
                    
                    # Essaie de placer le bateau
                    if self.plateau_joueur.placer_bateau(Bateau(nom, taille), x, y, horizontal):
                        break
                    else:
                        print("\nPosition invalide ! Réessayez.")
                except ValueError:
                    print("\nEntrée invalide ! Utilisez des nombres entre 0 et 9.")
    
    def placer_bateaux_ordinateur(self):
        """Place aléatoirement les bateaux de l'ordinateur"""
        print("\nL'ordinateur place ses bateaux...")
        for nom, taille in self.types_bateaux:
            while True:
                # Génère des coordonnées aléatoires
                x = random.randint(0, 9)
                y = random.randint(0, 9)
                horizontal = random.choice([True, False])
                
                if self.plateau_ordinateur.placer_bateau(Bateau(nom, taille), x, y, horizontal):
                    break
    
    def tour_joueur(self):
        """Gère le tour du joueur"""
        print("\nVotre tour!")
        while True:
            try:
                x = int(input("Ligne de tir (0-9): "))
                y = int(input("Colonne de tir (0-9): "))
                
                valide, message = self.plateau_ordinateur.recevoir_tir(x, y)
                print(message)
                
                if valide:
                    return self.verifier_victoire(self.plateau_ordinateur)
            except ValueError:
                print("Entrée invalide ! Utilisez des nombres entre 0 et 9.")
    
    def tour_ordinateur(self):
        """Gère le tour de l'ordinateur"""
        print("\nTour de l'ordinateur:")
        while True:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            
            valide, message = self.plateau_joueur.recevoir_tir(x, y)
            if valide:
                print(f"L'ordinateur tire en ({x}, {y}): {message}")
                return self.verifier_victoire(self.plateau_joueur)
    
    def verifier_victoire(self, plateau):
        """Vérifie si tous les bateaux sont coulés sur un plateau"""
        return all(bateau.est_coule() for bateau in plateau.bateaux)
    
    def jouer(self):
        """Lance une partie de bataille navale"""
        print("=== BATAILLE NAVALE ===")
        
        # Phase de placement
        self.placer_bateaux_joueur()
        self.placer_bateaux_ordinateur()
        
        # Boucle de jeu
        while True:
            # Affichage des plateaux
            print("\nVotre plateau:")
            self.plateau_joueur.afficher(True)
            print("\nPlateau de l'ordinateur:")
            self.plateau_ordinateur.afficher(False)
            
            # Tour du joueur
            if self.tour_joueur():
                print("\nFélicitations ! Vous avez gagné !")
                break
            
            # Tour de l'ordinateur
            if self.tour_ordinateur():
                print("\nL'ordinateur a gagné !")
                break

# Lancement du jeu
if __name__ == "__main__":
    jeu = BatailleNavale()
    jeu.jouer()