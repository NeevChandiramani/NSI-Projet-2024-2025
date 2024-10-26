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
        print ("   1 2 3 4 5 6 7 8 9 10")
        for i in range(self.taille) :
            print((i + 1), end = ' ')
            for j in range(self.taille) :
                case = self.grille[i][j]
                if not montrer_bateaux :
                    print(self.EAU, end = ' ')      # Affiche uniquement des vagues si montrer_bateaux est toujours = False
                else :
                    print(case, end = ' ')          # Affiche Les endroits où il y'a des bateaux quand montrer_bateaux = True
            print()


    def placer_bateau(self,bateau,x,y,horizontal):
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
        bateau.positions = positions_possibles # devient les position impossibles pour placer un autre bateau
        self.bateaux.append(bateau)
        return True                    
                                      


    
    def boulet_de_canon(self, x, y) :
        if not (1 <= x < self.taille and 1 <= y < self.taille) :    #Définir si le boulet est dans la grille
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
            ("Le Lafaux", 2)
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
                    orientation = input("Horizontal (oui/non)? ").lower()
                    horizontal = orientation == 'oui'
                    
                    # Essaie de placer le bateau
                    if self.plateau_joueur.placer_bateau(Bateau(nom, taille), x, y, horizontal):
                        break
                    else:
                        print("\nPosition invalide ! Réessayez.")
                except ValueError:
                   print("\nEntrée invalide ! Utilisez des nombres entre 1 et 10.")



        def placer_bateaux_ordinateur(self):
            print("\nL'ordinateur place ses bateaux...")
            for nom, taille in self.types_bateaux:
                while not self.plateau_ordinateur.placer_bateau(
                  Bateau(nom, taille),
                  random.randint(0, 9),
                  random.randint(0, 9),
                  random.choice([True, False])
                 ):
            pass
