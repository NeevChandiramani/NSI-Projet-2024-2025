import random
import time 


class Bateau:
    def __init__(self, nom, taille):
        self.nom = nom        # Nom du bateau (ex: "Le Charles de Gaulle")
        self.taille = taille  # Longueur du bateau
        self.positions = []   # Liste des coordonnées occupées par le bateau
        self.touches = []     # Liste des positions touchées par l'adversaire
    
    def est_coule(self):
        #Vérifie si le bateau est coulé (toutes les positions sont touchées)
        return len(self.touches) == self.taille
    
    def est_touche(self, x, y):
        #Vérifie les coordonnées x et y touchent un bateau
        if (x,y) in self.positions:
            return True 
        return False 


class Plateau:
    def __init__(self, taille=10):
        # Codes couleurs ANSI
        self.BLEU = '\033[94m'      # Eau en bleu
        self.GRIS = '\033[90m'      # Bateau en gris 
        self.ROUGE = '\033[91m'     # Tir touché en rouge
        self.JAUNE = '\033[93m'     # Tir raté en jaune
        self.RESET = '\033[0m'      # Réinitialiser la couleur

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

    def afficher(self, montrer_bateaux = False):
        # Afficher la grille 10x10
        print ("   0 1 2 3 4 5 6 7 8 9")
        for i in range(self.taille):
            print((i), end = '  ',)    # Normal la , ?
            for j in range(self.taille):
                case = self.grille[i][j]
                
                # Colorisation des cases
                if case == self.EAU:
                    print(f"{self.BLEU}~ {self.RESET}", end='')
                elif case == self.BATEAU and montrer_bateaux:
                    print(f"{self.GRIS}B {self.RESET}", end='')
                elif case == self.TOUCHE:
                    print(f"{self.ROUGE}X {self.RESET}", end='')
                elif case == self.RATE:
                    print(f"{self.JAUNE}O {self.RESET}", end='')
                else:
                    print(f"{self.BLEU}~ {self.RESET}", end='')
            print()

    def placer_bateau(self, bateau, x, y, horizontal):
        # Essaie de placer un bateau aux coordonnées données
        if not (0 <= x < self.taille and 0 <= y < self.taille):    #si x et y ne sont pas plus grand ou égal à 0 et strictement plus petit que 10
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
        bateau.positions = positions_possibles
        self.bateaux.append(bateau)
        return True

    def boulet_de_canon(self, x, y):
        # Vérifier que les coordonnées sont entre 0 et 9 inclues sinon return
        if not (0 <= x <= 9 and 0 <= y <= 9):
            return False, "Utilisez des chiffres entre 0 et 9"

        # Vérifier si la case a déjà été ciblée
        if self.grille[x][y] in [self.TOUCHE, self.RATE]:
            return False, "Un boulet de canon a déjà atterri ici !"
            
        # Vérifier l'emplacement de tous les bateaux pour savoir si un a été touché et lequel
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


class BatailleNavale:    # Class avec les méthodes principales du jeu
    def __init__(self):
        # Définition des deux plateaux identiques pour le joueur et l'ordinateur
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
        # Permet au joueur de placer ses bateaux
        print("\nPlacement de vos bateaux :")
        for nom, taille in self.types_bateaux:
            while True:
                self.plateau_joueur.afficher(True)
                print(f"\nPlacer le {nom} (taille: {taille})")

                # Try test si le joueur entre bien des chiffres entre 0 et 9 inclues
                try:
                    # Demande les coordonnées
                    x = int(input("Ligne (0-9) : "))
                    y = int(input("Colonne (0-9) : "))
                    
                    # Demande l'orientation
                    orientation = input("\nHorizontal (oui/non)? ").lower()
                    horizontal = orientation == 'oui'
                    
                    # Essaie de placer le bateau
                    if self.plateau_joueur.placer_bateau(Bateau(nom, taille), x, y, horizontal):
                        break
                    else:
                        print("\nPosition invalide ! Réessayez.")
                        
                # Except ValueError est exécutée si le joueur n'entre pas des chiffres
                except ValueError:
                   print("\nEntrée invalide ! Utilisez des nombres entre 0 et 9 : ")

    def placer_bateaux_ordinateur(self):
        # L'ordinateur place ses bateaux de manière aléatoire
        print("\nL'ordinateur place ses bateaux...")
        time.sleep(5)
        for nom, taille in self.types_bateaux:
            while not self.plateau_ordinateur.placer_bateau(
                Bateau(nom, taille),            # Nom du bateau
                random.randint(0, 9),           # Coordonées aléatoires de x
                random.randint(0, 9),           # Coordonées aléatoires de y
                random.choice([True, False])    # Choix horizontal ou non aléatoire
                ):
                    pass

    def tour_joueur(self):
        # Demande au joueur où il veut tirer son boulet
        print("\nC'est votre tour !")
        while True:
            x = int(input("Choisissez une ligne de tir entre 0 et 9 : "))
            y = int(input("Choisissez une colonne de tir entre 0 et 9 : "))
            valide, rep = self.plateau_ordinateur.boulet_de_canon(x, y)    # La méthode "Boulet_de_canon" renvoie deux arguments : Un booléen (ici "valide") et un message (ici "rep")
            if valide == False:
                print(rep)
            elif valide == True:
                print(rep)
                return self.verifier_victoire(self.plateau_ordinateur)

    def tour_ordinateur(self):
        # L'ordinateur tire de manière aléatoire sur le plateau
        print("\nC'est au tour de l'ordinateur.")
        time.sleep(4)
        while True:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            valide, rep = self.plateau_joueur.boulet_de_canon(x, y)
            if valide == True:
                print (f"L'ordinateur tire en ({x}, {y}) : {rep}")
                time.sleep(3)
                return self.verifier_victoire(self.plateau_joueur)

    def verifier_victoire(self, plateau):
        # Vérifie dans les bateaux du plateau si ils sont tous coulés
        for bateau in plateau.bateaux:
            if not bateau.est_coule():
                return False
        return True
    
    def jouer(self):
        # Lance la partie de bataille navale
        print("\n=== BATAILLE NAVALE ===")

        self.placer_bateaux_joueur()         # La fonctions demande au joueur ou il veut placer ses bateaux
        self.placer_bateaux_ordinateur()     # Place les bateaux de l'ordinateur aleatoirement sur sa grille
        
        while True:
            # Affichage des plateaux
            print("\nVotre plateau:")
            self.plateau_joueur.afficher(True)        # Le True modifie le "montrer_bateau" pour que les bateaux soient affichés
            print("\nPlateau de l'ordinateur:")
            self.plateau_ordinateur.afficher(False)   # Le False modifie la même chose pour que le joueur ne puisse pas voir les bateaux de l'ordinateur
              
            # Tour du joueur
            if self.tour_joueur():
                print("\nFélicitations ! Vous avez gagné !")
                print("\nLe plateau de l'ordinateur était:")
                self.plateau_ordinateur.afficher(True)
                break    # Arrête le tour du joueur pour passer à celui de l'ordinateur
            
            # Tour de l'ordinateur
            if self.tour_ordinateur():
                print("\nL'ordinateur a gagné !")
                print("\nLe plateau de l'ordinateur était:")
                self.plateau_ordinateur.afficher(True)
                break    # Arrête le tour de l'ordinateur pour passer à celui du joueur
                
# Lancement du jeu
if __name__ == "__main__":
    jeu = BatailleNavale()
    jeu.jouer()
