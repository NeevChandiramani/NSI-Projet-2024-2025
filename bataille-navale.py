import random
import time 


class Bateau:
    """ str, int -> None
    Classe représentant un bateau dans le jeu de bataille navale avec son nom et sa taille. """
    
    def __init__(self, nom, taille):
        """ Bateau, str, int -> None
        Initialise un nouveau bateau avec son nom et sa taille. """
        self.nom = nom
        self.taille = taille
        self.positions = []
        self.touches = []
    
    def est_coule(self):
        """ Bateau -> bool
        Renvoie True si le bateau est coulé (toutes les positions sont touchées), False sinon. """
        return len(self.touches) == self.taille
    
    def est_touche(self, x, y):
        """ Bateau, int, int -> bool
        Renvoie True si les coordonnées x et y touchent un bateau, False sinon. """
        if (x,y) in self.positions:
            return True 
        return False 


class Plateau:
    """ int -> None
    Classe représentant le plateau de jeu avec une taille par défaut de 10x10. """
    
    def __init__(self, taille=10):
        """ Plateau, int -> None
        Initialise un nouveau plateau de jeu avec la taille spécifiée. """
        self.BLEU = '\033[94m'
        self.GRIS = '\033[90m'
        self.ROUGE = '\033[91m'
        self.JAUNE = '\033[93m'
        self.RESET = '\033[0m'

        self.taille = taille
        self.grille = []
        for _ in range(taille):
            ligne = ['~'] * taille
            self.grille.append(ligne)
        self.bateaux = []
        
        self.EAU = '~'
        self.BATEAU = 'B'
        self.TOUCHE = 'X'
        self.RATE = 'O'

    def afficher(self, montrer_bateaux=False):
        """ Plateau, bool -> None
        Affiche l'état actuel du plateau avec les bateaux visibles si montrer_bateaux est True. """
        print ("   0 1 2 3 4 5 6 7 8 9")
        for i in range(self.taille):
            print((i), end = '  ',)
            for j in range(self.taille):
                case = self.grille[i][j]
                
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
        """ Plateau, Bateau, int, int, bool -> bool
        Essaie de placer un bateau aux coordonnées données et renvoie True si le placement est réussi, False sinon. """
        if not (0 <= x < self.taille and 0 <= y < self.taille):
            return False
    
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

    def boulet_de_canon(self, x, y):
        """ Plateau, int, int -> tuple[bool, str]
        Tire un boulet de canon aux coordonnées données et renvoie un tuple contenant un booléen (tir valide ou non)
        et un message décrivant le résultat du tir. """
        if not (0 <= x <= 9 and 0 <= y <= 9):
            return False, "Utilisez des chiffres entre 0 et 9"

        if self.grille[x][y] in [self.TOUCHE, self.RATE]:
            return False, "Un boulet de canon a déjà atterri ici !"
            
        for bateau in self.bateaux:
            if (x, y) in bateau.positions:
                bateau.touches.append((x, y))
                self.grille[x][y] = self.TOUCHE
                if bateau.est_coule():
                    return True, f"Touché Coulé, le {bateau.nom} est détruit !"
                return True, "Touché !"
        
        self.grille[x][y] = self.RATE
        return True, "Manqué !"        


class BatailleNavale:
    """ None -> None
    Classe principale gérant le déroulement d'une partie de bataille navale. """
    
    def __init__(self):
        """ BatailleNavale -> None
        Initialise une nouvelle partie avec les plateaux du joueur et de l'ordinateur. """
        self.plateau_joueur = Plateau()
        self.plateau_ordinateur = Plateau()
        
        self.types_bateaux = [
            ("Le Charles de Gaulle", 5),
            ("Le Mistral", 4),
            ("L'Aquitaine", 3),
            ("La Fayette", 3),
            ("Le Lafaux", 2),
            ("La Barque", 1)
        ]

    def placer_bateaux_joueur(self):
        """ BatailleNavale -> None
        Permet au joueur de placer interactivement ses bateaux sur son plateau. """
        print("\nPlacement de vos bateaux :\n")
        for nom, taille in self.types_bateaux:
            while True:
                self.plateau_joueur.afficher(True)
                print(f"\nPlacer le {nom} (taille: {taille})")

                try:
                    x, y = map(int, input("Entrez la Ligne (0-9) et la Colonne (0-9) séparées avec un espace : ").split())
                    
                    
                    orientation = input("\nHorizontal (oui/non)? ").lower()
                    horizontal = orientation == 'oui'
                    
                    if self.plateau_joueur.placer_bateau(Bateau(nom, taille), x, y, horizontal):
                        break
                    else:
                        print("\nPosition invalide ! Réessayez.")
                        
                except ValueError:
                   print("\nEntrée invalide ! Utilisez des nombres entre 0 et 9 : ")

    def placer_bateaux_ordinateur(self):
        """ BatailleNavale -> None
        Place aléatoirement les bateaux de l'ordinateur sur son plateau. """
        print("\nDe3pB0at place ses bateaux...")
        time.sleep(5)
        for nom, taille in self.types_bateaux:
            while not self.plateau_ordinateur.placer_bateau(
                Bateau(nom, taille),
                random.randint(0, 9),
                random.randint(0, 9),
                random.choice([True, False])
                ):
                    pass

    def tour_joueur(self):
        """ BatailleNavale -> bool
        Gère le tour du joueur et renvoie True si le joueur a gagné, False sinon. """
        print("\nC'est votre tour !")
        while True:
            try: 
                x, y = map(int, input("Entrez la Ligne (0-9) et la Colonne (0-9) du tir, séparées avec un espace : ").split())
                valide, rep = self.plateau_ordinateur.boulet_de_canon(x, y)
                if valide == False:
                    print(rep)
                elif valide == True:
                    print(rep)
                    return self.verifier_victoire(self.plateau_ordinateur)
            except ValueError:
                print("\nEntrée invalide ! Utilisez des nombres entre 0 et 9 : ")

    def tour_ordinateur(self):
        """ BatailleNavale -> bool
        Gère le tour de l'ordinateur et renvoie True si l'ordinateur a gagné, False sinon. """
        print("\nC'est au tour de l'ordinateur.")
        time.sleep(4)
        while True:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            valide, rep = self.plateau_joueur.boulet_de_canon(x, y)
            if valide == True:
                print (f"De3pB0at tire en ({x}, {y}) : {rep}")
                time.sleep(3)
                return self.verifier_victoire(self.plateau_joueur)

    def verifier_victoire(self, plateau):
        """ BatailleNavale, Plateau -> bool
        Renvoie True si tous les bateaux du plateau sont coulés, False sinon. """
        for bateau in plateau.bateaux:
            if not bateau.est_coule():
                return False
        return True
    
    def jouer(self):
        """ BatailleNavale -> None
        Lance et gère une partie complète de aavale. """
        print("\n=== BATAILLE NAVALE ===")
        print("\nVous allez affronter une intellingence artificielle de haut niveau dans ce jeu de bataille navale.")
        print("\nElle est nomée : 'De3pB0at'")

        self.placer_bateaux_joueur()
        self.placer_bateaux_ordinateur()
        
        while True:
            print("\nVotre plateau:")
            self.plateau_joueur.afficher(True)
            print("\nPlateau de De3pB0at:")
            self.plateau_ordinateur.afficher(False)
              
            if self.tour_joueur():
                print("\nFélicitations ! Vous avez gagné !")
                print("\nLe plateau de De3pB0at était:")
                self.plateau_ordinateur.afficher(True)
                break
            
            if self.tour_ordinateur():
                print("\nDe3pB0at a gagné !")
                print("\nLe plateau de De3pB0at était:")
                self.plateau_ordinateur.afficher(True)
                break
                
# Lancement du jeu
if __name__ == "__main__":
    jeu = BatailleNavale()
    jeu.jouer()