import random
import enum

class Player:
    def __init__(self, name):
        self.name = name
        self.board = Board()
    
    def place_ships(self):
        print(f"{self.name}, placez vos bateaux sur votre grille.")
        for ship in ShipType:
            size = ship.value
            while True:
                row, col = map(int, input(f"Entrez les coordonnées de début pour le bateau {ship} (format: row col): ").split())
                horizontal = input("Horizontal or Vertical? (h/v): ").lower() == 'h'
                if self.board.place_ship(row, col, size, horizontal):
                    break
                else:
                    print("Placement invalide, réessayez.")
    
    def attack(self, other_player):
        row, col = map(int, input("Entrez les coordonnées de l'attaque: ").split())
        return self.board.attack(row, col, other_player)

class ShipType(enum.Enum):
    Carrier = 5
    Battleship = 4
    Cruiser = 3
    Submarine = 3
    Destroyer = 2

class Board:
    def __init__(self):
        self.grid = [['.' for _ in range(10)] for _ in range(10)]
    
    def place_ship(self, row, col, size, horizontal):
        if horizontal:
            if col + size > 10:
                return False
            for i in range(size):
                if self.grid[row][col+i] != '.':
                    return False
            for i in range(size):
                self.grid[row][col+i] = 'S'
        else:
            if row + size > 10:
                return False
            for i in range(size):
                if self.grid[row+i][col] != '.':
                    return False
            for i in range(size):
                self.grid[row+i][col] = 'S'
        return True
    
    def attack(self, row, col, other_player):
        if self.grid[row][col] == 'S':
            self.grid[row][col] = 'X'
            print("Touché!")
            hit = True
            for r in range(10):
                for c in range(10):
                    if other_player.board.grid[r][c] == 'S':
                        return False
            print("Le bateau coulé!")
            return True
        else:
            self.grid[row][col] = 'O'
            print("Manqué.")
            return False
    
    def display(self):
        for row in self.grid:
            print(' '.join(row))

class Game:
    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)
    
    def play(self):
        print("Début de la partie!")
        for _ in range(2):
            self.player1.place_ships()
            self.player2.place_ships()
        
        current_attacker = random.choice([self.player1, self.player2])
        other_player = self.player1 if current_attacker == self.player2 else self.player2
        
        while True:
            print(f"{current_attacker.name}, c'est votre tour d'attaquer.")
            result = current_attacker.attack(other_player)
            if result:
                current_attacker, other_player = other_player, current_attacker
            else:
                break
        
        print("Partie terminée!")

if __name__ == "__main__":
    player1_name = input("Entrez le nom du joueur 1: ")
    player2_name = input("Entrez le nom du joueur 2: ")
    game = Game(player1_name, player2_name)
    game.play()