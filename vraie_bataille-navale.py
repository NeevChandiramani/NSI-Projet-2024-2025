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