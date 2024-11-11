from bataille_navale import Bateau, Plateau, BatailleNavale

def test_bateau_creation():
    """ None -> None
    Teste la création d'un bateau en vérifiant que ses attributs sont correctement initialisés.
    Vérifie le nom, la taille et que les listes de positions et touches sont vides. """
    bateau = Bateau("Le Charles de Gaulle", 5)
    assert bateau.nom == "Le Charles de Gaulle"
    assert bateau.taille == 5
    assert len(bateau.positions) == 0
    assert len(bateau.touches) == 0

def test_bateau_est_coule():
    """ None -> None
    Teste la méthode est_coule() d'un bateau.
    Vérifie qu'un bateau est considéré comme coulé uniquement quand toutes ses positions sont touchées. """
    bateau = Bateau("Le Charles de Gaulle", 5)
    # Test avec toutes les positions touchées
    bateau.touches = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)]
    assert bateau.est_coule()
    # Test avec positions partiellement touchées
    bateau.touches = [(0, 0), (0, 1), (0, 2), (0, 3)]
    assert not bateau.est_coule()

def test_bateau_est_touche():
    """ None -> None
    Teste la méthode est_touche() d'un bateau.
    Vérifie la détection correcte des positions touchées et non touchées. """
    bateau = Bateau("Le Charles de Gaulle", 5)
    bateau.positions = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)]
    # Test avec une position occupée par le bateau
    assert bateau.est_touche(0, 0)
    # Test avec une position non occupée par le bateau
    assert not bateau.est_touche(1, 0)

def test_plateau_creation():
    """ None -> None
    Teste la création d'un plateau en vérifiant sa taille et l'initialisation de la grille.
    S'assure que toutes les cases contiennent initialement de l'eau. """
    plateau = Plateau(10)
    assert plateau.taille == 10
    assert len(plateau.grille) == 10
    # Vérifie que chaque case contient bien de l'eau au départ
    for ligne in plateau.grille:
        for case in ligne:
            assert case == plateau.EAU

def test_plateau_placer_bateau():
    """ None -> None
    Teste le placement des bateaux sur le plateau.
    Vérifie les placements valides et invalides, horizontaux et verticaux. """
    plateau = Plateau(10)
    bateau = Bateau("Le Charles de Gaulle", 5)
    
    # Test d'un placement horizontal valide
    assert plateau.placer_bateau(bateau, 0, 0, True)
    assert bateau.positions == [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)]
    
    # Test d'un placement invalide (hors grille)
    bateau2 = Bateau("Test", 5)
    assert not plateau.placer_bateau(bateau2, 0, 6, True)
    
    # Test d'un placement vertical valide
    bateau3 = Bateau("Test2", 3)
    assert plateau.placer_bateau(bateau3, 2, 0, False)
    assert bateau3.positions == [(2, 0), (3, 0), (4, 0)]

def test_plateau_boulet_de_canon():
    """ None -> None
    Teste la fonction de tir (boulet_de_canon).
    Vérifie les cas de touché, manqué et coulé. """
    plateau = Plateau(10)
    bateau = Bateau("Le Charles de Gaulle", 5)
    plateau.placer_bateau(bateau, 0, 0, True)
    
    # Test d'un tir touchant un bateau
    valide, rep = plateau.boulet_de_canon(0, 0)
    assert valide
    assert rep == "Touché !"
    assert (0, 0) in bateau.touches
    
    # Test d'un tir dans l'eau
    valide, rep = plateau.boulet_de_canon(1, 0)
    assert valide
    assert rep == "Manqué !"
    
    # Test de tous les tirs nécessaires pour couler le bateau
    valide, rep = plateau.boulet_de_canon(0, 1)
    assert valide
    valide, rep = plateau.boulet_de_canon(0, 2)
    assert valide
    valide, rep = plateau.boulet_de_canon(0, 3)
    assert valide
    valide, rep = plateau.boulet_de_canon(0, 4)
    assert valide
    assert "Coulé" in rep

def test_plateau_attributs_couleur():
    """ None -> None
    Teste la présence des attributs de couleur nécessaires pour l'affichage. """
    plateau = Plateau()
    # Vérifie que tous les attributs de couleur sont présents
    assert hasattr(plateau, 'BLEU')
    assert hasattr(plateau, 'GRIS')
    assert hasattr(plateau, 'ROUGE')
    assert hasattr(plateau, 'JAUNE')
    assert hasattr(plateau, 'RESET')

def test_bataille_navale_creation():
    """ None -> None
    Teste la création d'une partie de bataille navale.
    Vérifie l'initialisation des plateaux et la liste des types de bateaux. """
    jeu = BatailleNavale()
    assert isinstance(jeu.plateau_joueur, Plateau)
    assert isinstance(jeu.plateau_ordinateur, Plateau)
    assert len(jeu.types_bateaux) == 6
    # Vérifie la présence des bateaux principaux
    assert ("Le Charles de Gaulle", 5) in jeu.types_bateaux
    assert ("Le Mistral", 4) in jeu.types_bateaux

def test_plateau_afficher():
    """ None -> None
    Teste la fonction d'affichage du plateau.
    Vérifie que l'affichage fonctionne avec et sans bateaux visibles. """
    plateau = Plateau(2)
    # Test d'affichage basique
    plateau.afficher(False)
    plateau.afficher(True)
    # Test d'affichage avec un bateau
    bateau = Bateau("Test", 1)
    plateau.placer_bateau(bateau, 0, 0, True)
    plateau.afficher(True)

def test_verifier_victoire():
    """ None -> None
    Teste la vérification de victoire.
    Vérifie les conditions de victoire avec un ou plusieurs bateaux. """
    jeu = BatailleNavale()
    plateau = jeu.plateau_joueur
    
    # Test avec un bateau non coulé
    bateau1 = Bateau("Test1", 2)
    plateau.placer_bateau(bateau1, 0, 0, True)
    assert not jeu.verifier_victoire(plateau)
    
    # Test avec un bateau coulé
    bateau1.touches = [(0, 0), (0, 1)]
    assert jeu.verifier_victoire(plateau)
    
    # Test avec plusieurs bateaux
    bateau2 = Bateau("Test2", 1)
    plateau.placer_bateau(bateau2, 2, 0, True)
    assert not jeu.verifier_victoire(plateau)
    bateau2.touches = [(2, 0)]
    assert jeu.verifier_victoire(plateau)

def test_placer_bateaux_ordinateur():
    """ None -> None
    Teste le placement automatique des bateaux par l'ordinateur.
    Vérifie que tous les bateaux sont placés correctement. """
    jeu = BatailleNavale()
    jeu.placer_bateaux_ordinateur()
    
    # Vérifie le nombre de bateaux placés
    assert len(jeu.plateau_ordinateur.bateaux) == len(jeu.types_bateaux)
    
    # Vérifie la validité des positions
    for bateau in jeu.plateau_ordinateur.bateaux:
        for x, y in bateau.positions:
            assert 0 <= x < 10
            assert 0 <= y < 10
            assert jeu.plateau_ordinateur.grille[x][y] == jeu.plateau_ordinateur.BATEAU

def test_tour_ordinateur():
    """ None -> None
    Teste le tour de jeu de l'ordinateur.
    Vérifie que l'ordinateur effectue un tir valide. """
    jeu = BatailleNavale()
    bateau = Bateau("Test", 1)
    jeu.plateau_joueur.placer_bateau(bateau, 0, 0, True)
    
    # Fait jouer l'ordinateur
    resultat = jeu.tour_ordinateur()
    
    # Compte les tirs effectués
    nb_touches = 0
    nb_rates = 0
    for ligne in jeu.plateau_joueur.grille:
        nb_touches += ligne.count(jeu.plateau_joueur.TOUCHE)
        nb_rates += ligne.count(jeu.plateau_joueur.RATE)
    
    # Vérifie qu'un seul tir a été effectué
    assert nb_touches + nb_rates == 1

def test_boulet_canon_cases_invalides():
    """ None -> None
    Teste les cas limites et invalides de la fonction boulet_de_canon.
    Vérifie la gestion des tirs hors grille et des tirs répétés. """
    plateau = Plateau()
    # Tests des tirs hors limites
    valide, message = plateau.boulet_de_canon(-1, 0)
    assert not valide
    assert "Utilisez des chiffres entre 0 et 9" in message
    
    valide, message = plateau.boulet_de_canon(10, 0)
    assert not valide
    assert "Utilisez des chiffres entre 0 et 9" in message
    
    # Test de tir sur une case déjà touchée
    plateau.grille[5][5] = plateau.TOUCHE
    valide, message = plateau.boulet_de_canon(5, 5)
    assert not valide
    assert "Un boulet de canon a déjà atterri ici !" in message

def test_placer_bateau_positions_invalides():
    """ None -> None
    Teste les cas limites et invalides du placement des bateaux.
    Vérifie la gestion des positions hors grille et des chevauchements. """
    plateau = Plateau()
    bateau = Bateau("Test", 3)
    
    # Tests des placements hors grille
    assert not plateau.placer_bateau(bateau, -1, 0, True)
    assert not plateau.placer_bateau(bateau, 0, -1, True)
    assert not plateau.placer_bateau(bateau, 10, 0, True)
    assert not plateau.placer_bateau(bateau, 0, 10, True)
    
    # Tests des dépassements de grille
    assert not plateau.placer_bateau(bateau, 0, 8, True)
    assert not plateau.placer_bateau(bateau, 8, 0, False)
    
    # Test de chevauchement de bateaux
    bateau1 = Bateau("Test1", 2)
    plateau.placer_bateau(bateau1, 0, 0, True)
    assert not plateau.placer_bateau(bateau, 0, 0, True)

def test_types_bateaux():
    """ None -> None
    Teste la liste des types de bateaux disponibles dans le jeu.
    Vérifie que tous les bateaux prévus sont présents avec leurs caractéristiques. """
    jeu = BatailleNavale()
    # Liste des bateaux attendus avec leurs caractéristiques
    bateaux_attendus = [
        ("Le Charles de Gaulle", 5),
        ("Le Mistral", 4),
        ("L'Aquitaine", 3),
        ("La Fayette", 3),
        ("Le Lafaux", 2),
        ("La Barque", 1)
    ]
    # Vérifie la présence de chaque bateau
    for bateau in bateaux_attendus:
        assert bateau in jeu.types_bateaux

# Point d'entrée pour l'exécution des tests
if __name__ == "__main__":
    # Exécution de tous les tests unitaires
    test_bateau_creation()
    test_bateau_est_coule()
    test_bateau_est_touche()
    test_plateau_creation()
    test_plateau_placer_bateau()
    test_plateau_boulet_de_canon()
    test_bataille_navale_creation()
    test_plateau_afficher()
    test_verifier_victoire()
    test_placer_bateaux_ordinateur()
    test_tour_ordinateur()
    test_boulet_canon_cases_invalides()
    test_placer_bateau_positions_invalides()
    test_plateau_attributs_couleur()
    test_types_bateaux()
    
    print("Tous les tests ont réussi !")