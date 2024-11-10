from bataille_navale import Bateau, Plateau, BatailleNavale

def test_bateau_creation():
    bateau = Bateau("Le Charles de Gaulle", 5)
    assert bateau.nom == "Le Charles de Gaulle"
    assert bateau.taille == 5
    assert len(bateau.positions) == 0
    assert len(bateau.touches) == 0

def test_bateau_est_coule():
    bateau = Bateau("Le Charles de Gaulle", 5)
    bateau.touches = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)]
    assert bateau.est_coule()
    bateau.touches = [(0, 0), (0, 1), (0, 2), (0, 3)]
    assert not bateau.est_coule()

def test_bateau_est_touche():
    bateau = Bateau("Le Charles de Gaulle", 5)
    bateau.positions = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)]
    assert bateau.est_touche(0, 0)
    assert not bateau.est_touche(1, 0)

def test_plateau_creation():
    plateau = Plateau(10)
    assert plateau.taille == 10
    assert len(plateau.grille) == 10
    # Vérifier que la grille est bien initialisée avec de l'eau
    for ligne in plateau.grille:
        for case in ligne:
            assert case == plateau.EAU

def test_plateau_placer_bateau():
    plateau = Plateau(10)
    bateau = Bateau("Le Charles de Gaulle", 5)
    
    # Test placement horizontal valide
    assert plateau.placer_bateau(bateau, 0, 0, True)
    assert bateau.positions == [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)]
    
    # Test placement invalide (hors grille)
    bateau2 = Bateau("Test", 5)
    assert not plateau.placer_bateau(bateau2, 0, 6, True)
    
    # Test placement vertical valide
    bateau3 = Bateau("Test2", 3)
    assert plateau.placer_bateau(bateau3, 2, 0, False)
    assert bateau3.positions == [(2, 0), (3, 0), (4, 0)]

def test_plateau_boulet_de_canon():
    plateau = Plateau(10)
    bateau = Bateau("Le Charles de Gaulle", 5)
    plateau.placer_bateau(bateau, 0, 0, True)
    
    # Test touché
    valide, rep = plateau.boulet_de_canon(0, 0)
    assert valide
    assert rep == "Touché !"
    assert (0, 0) in bateau.touches
    
    # Test manqué
    valide, rep = plateau.boulet_de_canon(1, 0)
    assert valide
    assert rep == "Manqué !"
    
    # Test touché coulé
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
    plateau = Plateau()
    assert hasattr(plateau, 'BLEU')
    assert hasattr(plateau, 'GRIS')
    assert hasattr(plateau, 'ROUGE')
    assert hasattr(plateau, 'JAUNE')
    assert hasattr(plateau, 'RESET')

def test_bataille_navale_creation():
    jeu = BatailleNavale()
    assert isinstance(jeu.plateau_joueur, Plateau)
    assert isinstance(jeu.plateau_ordinateur, Plateau)
    assert len(jeu.types_bateaux) == 6
    # Vérifie la présence des bateaux avec leurs tailles
    assert ("Le Charles de Gaulle", 5) in jeu.types_bateaux
    assert ("Le Mistral", 4) in jeu.types_bateaux

def test_plateau_afficher():
    plateau = Plateau(2)
    # On vérifie juste que la fonction s'exécute sans erreur
    plateau.afficher(False)
    plateau.afficher(True)
    # Place un bateau et vérifie l'affichage avec bateaux
    bateau = Bateau("Test", 1)
    plateau.placer_bateau(bateau, 0, 0, True)
    plateau.afficher(True)

def test_verifier_victoire():
    jeu = BatailleNavale()
    plateau = jeu.plateau_joueur
    
    # Test sans bateaux coulés
    bateau1 = Bateau("Test1", 2)
    plateau.placer_bateau(bateau1, 0, 0, True)
    assert not jeu.verifier_victoire(plateau)
    
    # Test avec tous les bateaux coulés
    bateau1.touches = [(0, 0), (0, 1)]
    assert jeu.verifier_victoire(plateau)
    
    # Test avec plusieurs bateaux
    bateau2 = Bateau("Test2", 1)
    plateau.placer_bateau(bateau2, 2, 0, True)
    assert not jeu.verifier_victoire(plateau)
    bateau2.touches = [(2, 0)]
    assert jeu.verifier_victoire(plateau)

def test_placer_bateaux_ordinateur():
    jeu = BatailleNavale()
    jeu.placer_bateaux_ordinateur()
    
    # Vérifier que tous les bateaux ont été placés
    assert len(jeu.plateau_ordinateur.bateaux) == len(jeu.types_bateaux)
    
    # Vérifier que les positions sont valides
    for bateau in jeu.plateau_ordinateur.bateaux:
        for x, y in bateau.positions:
            assert 0 <= x < 10
            assert 0 <= y < 10
            assert jeu.plateau_ordinateur.grille[x][y] == jeu.plateau_ordinateur.BATEAU

def test_tour_ordinateur():
    jeu = BatailleNavale()
    bateau = Bateau("Test", 1)
    jeu.plateau_joueur.placer_bateau(bateau, 0, 0, True)
    
    # Faire jouer l'ordinateur
    resultat = jeu.tour_ordinateur()
    
    # Vérifier qu'un tir a été effectué
    nb_touches = 0
    nb_rates = 0
    for ligne in jeu.plateau_joueur.grille:
        nb_touches += ligne.count(jeu.plateau_joueur.TOUCHE)
        nb_rates += ligne.count(jeu.plateau_joueur.RATE)
    
    assert nb_touches + nb_rates == 1

def test_boulet_canon_cases_invalides():
    plateau = Plateau()
    # Test de tirs hors limites
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
    plateau = Plateau()
    bateau = Bateau("Test", 3)
    
    # Test placement hors grille (négatif)
    assert not plateau.placer_bateau(bateau, -1, 0, True)
    assert not plateau.placer_bateau(bateau, 0, -1, True)
    
    # Test placement hors grille (trop grand)
    assert not plateau.placer_bateau(bateau, 10, 0, True)
    assert not plateau.placer_bateau(bateau, 0, 10, True)
    
    # Test placement qui dépasse la grille horizontalement
    assert not plateau.placer_bateau(bateau, 0, 8, True)
    
    # Test placement qui dépasse la grille verticalement
    assert not plateau.placer_bateau(bateau, 8, 0, False)
    
    # Test placement sur un bateau existant
    bateau1 = Bateau("Test1", 2)
    plateau.placer_bateau(bateau1, 0, 0, True)
    assert not plateau.placer_bateau(bateau, 0, 0, True)

def test_types_bateaux():
    jeu = BatailleNavale()
    # Vérifie tous les types de bateaux
    bateaux_attendus = [
        ("Le Charles de Gaulle", 5),
        ("Le Mistral", 4),
        ("L'Aquitaine", 3),
        ("La Fayette", 3),
        ("Le Lafaux", 2),
        ("La Barque", 1)
    ]
    for bateau in bateaux_attendus:
        assert bateau in jeu.types_bateaux

if __name__ == "__main__":
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