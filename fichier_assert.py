
import random
from bataille_navale import Bateau, Plateau, BatailleNavale # type: ignore

# Tests pour la classe Bateau
def test_bateau():
    # Test de la méthode est_coule
    bateau = Bateau("Navire Test", 3)
    bateau.touches = [(0, 0), (0, 1), (0, 2)]
    assert bateau.est_coule() == True, "Le bateau devrait être considéré comme coulé"
    bateau.touches = [(0, 0), (0, 1)]
    assert bateau.est_coule() == False, "Le bateau ne devrait pas être considéré comme coulé"

    # Test de la méthode est_touche
    bateau.positions = [(1, 1), (1, 2), (1, 3)]
    assert bateau.est_touche(1, 1) == True, "Le bateau devrait être touché à la position (1,1)"
    assert bateau.est_touche(2, 2) == False, "Le bateau ne devrait pas être touché à la position (2,2)"


# Tests pour la classe Plateau
def test_plateau():
    plateau = Plateau(taille=5)
    bateau = Bateau("Mini Navire", 2)
    
    # Test de la méthode placer_bateau
    succes = plateau.placer_bateau(bateau, 0, 0, horizontal=True)
    assert succes == True, "Le bateau devrait être placé avec succès à (0,0) horizontalement"
    assert plateau.grille[0][0] == 'B' and plateau.grille[0][1] == 'B', "La grille devrait afficher le bateau à (0,0) et (0,1)"

    # Test de la méthode boulet_de_canon
    succes, message = plateau.boulet_de_canon(0, 0)
    assert succes == True and message == "Touché !", "Le tir à (0,0) devrait être un succès avec un message de 'Touché !'"

# Tests pour la classe BatailleNavale
def test_bataille_navale():
    jeu = BatailleNavale()

    # Test de la méthode verifier_victoire
    plateau_test = Plateau()
    bateau_test = Bateau("Test", 2)
    plateau_test.placer_bateau(bateau_test, 0, 0, horizontal=True)
    bateau_test.touches = [(0, 0), (0, 1)]
    assert jeu.verifier_victoire(plateau_test) == True, "Tous les bateaux devraient être coulés, donc victoire"

    bateau_test.touches = [(0, 0)]
    assert jeu.verifier_victoire(plateau_test) == False, "Tous les bateaux ne sont pas coulés, donc pas de victoire"

# Exécuter tous les tests
print(test_bateau())
print(test_plateau())
print(test_bataille_navale())
print("Tous les tests sont passés avec succès.")


