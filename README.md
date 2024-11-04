# Bataille Navale - Jeu en Console Python 🚢

Un jeu de bataille navale classique en console permettant d'affronter l'ordinateur. Le jeu est entièrement en français et utilise un affichage coloré pour une meilleure expérience utilisateur.

## 📋 Prérequis

- Un terminal supportant les codes de couleur ANSI
- Mettre le terminal dans une taille suffisante afin de bien voir les plateaux 

## 🛠️ Installation

1. Clonez ce dépôt ou téléchargez le fichier `bataille-navale.py`
2. Aucune dépendance externe n'est requise, le jeu utilise uniquement des modules Python standards

## 🎮 Comment jouer

1. Lancez le jeu en exécutant :
```bash
python bataille-navale.py
```

2. Placez vos bateaux selon les instructions :
   - Entrez les coordonnées (ligne et colonne entre 0 et 9)
   - Choisissez l'orientation (horizontale ou verticale)
   - Les bateaux à placer sont :
     - Le Charles de Gaulle (5 cases)
     - Le Mistral (4 cases)
     - L'Aquitaine (3 cases)
     - La Fayette (3 cases)
     - Le Lafaux (2 cases)
     - La Barque (1 case)

3. Pendant la partie :
   - Votre plateau est affiché avec vos bateaux (B)
   - Le plateau de l'ordinateur est masqué
   - Le plateau est marqué par :
     - ~ : Eau
     - O : Tir manqué
     - X : Tir touché
     - B : Bateau

   - À chaque tour, entrez les coordonnées de votre tir (ligne et colonne)

## 🎯 Règles du jeu

- Les joueurs tirent à tour de rôle
- Un message indique si le tir a touché, manqué ou coulé un navire
- Le premier joueur qui coule tous les bateaux adverses gagne la partie
- Il n'est pas possible de tirer deux fois au même endroit

## 🐛 Bugs connus

1. L'ordinateur tire de manière complètement aléatoire, même après avoir touché un bateau
2. Le programme plante si l'utilisateur entre une valeur non numérique pour les tirs
3. ...

## 🚀 Évolutions possibles

1. Amélioration de l'IA de l'ordinateur :
   - Tirer logiquement autour d'un bateau touché
   - Implémenter une stratégie de tir plus élaborée

2. Ajout de fonctionnalités :
   - Mode multijoueur local
   - Sauvegarde/chargement de partie
   - Statistiques de jeu (nombre de coups, pourcentage de réussite)
   - Différents niveaux de difficulté

3. Interface :
   - Version graphique avec PyGame
   - Ajout d'effets sonores
   - Animation des tirs
   - Utilisation d'images pour l'affichage des bateaux

4. Gameplay :
   - Ajout de capacités spéciales pour certains bateaux
   - Ajout de points de vie pour les bateaux
   - Mode "bataille rapide" avec moins de bateaux
   - Règle de placement avec espacement obligatoire entre les bateaux

5. Documentation :
   - Traduction en anglais
   - Ajout de tests unitaires
   - Documentation du code avec docstrings complets

## 📝 Licence

Ce projet est distribué sous licence libre pour un projet de NSI de terminale. N'hésitez pas à l'utiliser et à le modifier selon vos besoins.
