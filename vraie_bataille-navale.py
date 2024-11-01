import random
import time 

class Bateau:
    def __init__(self, nom, taille):
        self.nom = nom        # Nom du bateau (ex: "Porte-avions")
        self.taille = taille  # Longueur du bateau
        self.positions = []   # Liste des coordonnées occupées par le bateau
        self.touches = []     # Liste des positions touchées par l'adversaire
    
    
    def est_coule(self):
        """Vérifie si le bateau est coulé (toutes les positions sont touchées)"""
        return len(self.touches) == self.taille
    
    def est_touche(self,x,y):
        if (x,y) in self.positions:
            return True 
        return False 
    


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
        print ("   1 2 3 4 5 6 7 8 9 10")
        for i in range(self.taille) :
            print((i + 1), end = '  ',)
            for j in range(self.taille) :
                case = self.grille[i][j]
                if not montrer_bateaux and case == self.BATEAU :
                    print(self.EAU, end = ' ')      # Affiche uniquement des vagues si montrer_bateaux est toujours = False
                else :
                    print(case, end = ' ')          # Affiche Les endroits où il y'a des bateaux quand montrer_bateaux = True
            print()


    def placer_bateau(self, bateau, x, y, horizontal):
        """Essaie de placer un bateau aux coordonnées données"""
        # Ajuster les coordonnées (1-10 -> 0-9)
        x = x - 1
        y = y - 1
        
        if not (0 <= x < self.taille and 0 <= y < self.taille):
            return False
    
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
        bateau.positions = positions_possibles # devient les position impossibles pour placer un autre bateau
        self.bateaux.append(bateau)
        return True

    def boulet_de_canon(self, x, y):
        """
        Lance un boulet de canon aux coordonnées spécifiées
        
        Args:
            x (int): Ligne (1-10)
            y (int): Colonne (1-10)
            
        Returns:
            bool: True si le tir est valide (touché ou manqué), False si invalide
        """
        # Vérifier que les coordonnées sont dans la plage 1-10
        if not (1 <= x <= 10 and 1 <= y <= 10):
            return False, "Utilisez des chiffres entre 1 et 10"

        # Ajuster les coordonnées pour l'index 0-based
        x = x - 1
        y = y - 1
        
        # Vérifier si la case a déjà été ciblée
        if self.grille[x][y] in [self.TOUCHE, self.RATE]:
            return False, "Un boulet de canon a déjà atterri ici !"
            
        # Vérifier tous les bateaux
        for bateau in self.bateaux:
            if (x, y) in bateau.positions:
                bateau.touches.append((x, y))
                self.grille[x][y] = self.TOUCHE
                if bateau.est_coule():
                    return True, f"Touché Coulé, le {bateau.nom} est détruit !"
                return True, "Touché !"
        
        # Si aucun bateau n'est touché
        self.grille[x][y] = self.RATE
        return True, "Manqué !"        
                                      



class BatailleNavale:
    def __init__(self):
        self.plateau_joueur = Plateau()
        self.plateau_ordinateur = Plateau()
        
        # Définition des bateaux du jeu
        self.types_bateaux = [
            ("Le Charles de Gaulle", 5),
            ("Le Mistral", 4),
            ("L'Aquitaine", 3),
            ("La Fayette", 3),
            ("Le Lafaux", 2),
            ("La Barque", 1)
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
                    x = int(input("Ligne (1-10): "))
                    y = int(input("Colonne (1-10): "))
                    
                    # Demande l'orientation
                    orientation = input("\nHorizontal (oui/non)? ").lower()
                    horizontal = orientation == 'oui'
                    
                    # Essaie de placer le bateau
                    if self.plateau_joueur.placer_bateau(Bateau(nom, taille), x, y, horizontal):
                        break
                    else:
                        print("\nPosition invalide ! Réessayez.")
                except ValueError:
                   print("\nEntrée invalide ! Utilisez des nombres entre 1 et 10 : ")



    def placer_bateaux_ordinateur(self):
        print("\nL'ordinateur place ses bateaux...")
        time.sleep(5)
        for nom, taille in self.types_bateaux:
            while not self.plateau_ordinateur.placer_bateau(
                Bateau(nom, taille),
                random.randint(1, 10),
                random.randint(1, 10),
                random.choice([True, False])
                ):
                    pass

    def tour_joueur(self) :
        print("\nC'est votre tour !")
        while True :
            x = int(input("Choisissez une ligne de tir entre 1 et 10 : "))
            y = int(input("Choisissez une colonne de tir entre 1 et 10 : "))
            valide, rep = self.plateau_ordinateur.boulet_de_canon(x, y)
            if valide == False :
                print(rep)
            elif valide == True :
                print(rep)
                return self.verifier_victoire(self.plateau_ordinateur)
    
                
    def tour_ordinateur(self) :
        print("\nC'est au tour de l'ordinateur.")
        time.sleep(4)
        while True :
            x = random.randint(1, 10)
            y = random.randint(1, 10)
            valide, rep = self.plateau_joueur.boulet_de_canon(x, y)
            if valide == True :
                print (f"L'ordinateur tire en ({x}, {y}) : {rep}")
                time.sleep(3)
                return self.verifier_victoire(self.plateau_joueur)

    def verifier_victoire(self, plateau):
        """
        Vérifie si tous les bateaux d'un plateau sont coulés
        
        Args:
            plateau (Plateau): Le plateau à vérifier
            
        Returns:
            bool: True si tous les bateaux sont coulés, False sinon
        """
        # La meilleure façon est de vérifier si tous les bateaux sont coulés
        for bateau in plateau.bateaux:
            if not bateau.est_coule():
                return False
        return True
    
    def jouer(self):
        """Lance une partie de bataille navale"""
        print("\n=== BATAILLE NAVALE ===")

        self.placer_bateaux_joueur() # La fonctions demande au joueur ou il veut placer ses bateaux
        self.placer_bateaux_ordinateur() # place les bateaux de l'ordinateur aleatoirement sur sa grille
        
        while True:
            # Affichage des plateaux
            print("\nVotre plateau:")
            self.plateau_joueur.afficher(True)
            print("\nPlateau de l'ordinateur:")
            self.plateau_ordinateur.afficher(False)
              
            # Tour du joueur
            if self.tour_joueur():
                print("\nFélicitations ! Vous avez gagné !")
                print("\nLe plateau de l'ordinateur était:")
                self.plateau_ordinateur.afficher(True)
                break
            
            # Tour de l'ordinateur
            if self.tour_ordinateur():
                print("\nL'ordinateur a gagné !")
                print("\nLe plateau de l'ordinateur était:")
                self.plateau_ordinateur.afficher(True)
                break
                

# Lancement du jeu
if __name__ == "__main__": # Vérifie si le fichier est exécuté directement ou s'il est importpé. Si le jeu est exécuté directement, le jeu est lancé.
    jeu = BatailleNavale() # Crée une instance jeu de la classe BatailleNavale 
    jeu.jouer() # Appel à la méthode jouer de la classe BatailleNavale pour lancer le jeu