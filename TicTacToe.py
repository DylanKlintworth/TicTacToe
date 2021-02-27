class Player:

    def __init__(self, gameboard=None, name="Player", team="x"):
        self.name = name
        self.team = team
        self.gameboard = gameboard

    def get_score(self):
        return self.score

    def get_name(self):
        return self.name

    def get_team(self):
        return self.team

    def take_turn(self, location):
        if int(location) not in range(1, 10):
            raise Exception("Location is not valid.")
        elif self.gameboard.grid[location] != "-":
            raise Exception("Location already used.")
        else:
            self.gameboard.grid[location] = self.team

    def __str__(self):
        return f"Player name: {self.name}, Team: {self.team}"


class GameBoard:

    def __init__(self):
        self.grid = {
            "1": "-",
            "2": "-",
            "3": "-",
            "4": "-",
            "5": "-",
            "6": "-",
            "7": "-",
            "8": "-",
            "9": "-"
        }

    def zero(self):
        for x in self.grid:
            self.grid[x] = "-"

    def __str__(self):
        temp = ""
        for x in self.grid:
            if int(x) in [4, 7]:
                temp = temp + "\n"
            temp = temp + f"{self.grid[x]} "
        return temp


class Game:

    def __init__(self, gameboard=GameBoard(), players=list()):
        self.gameboard = gameboard
        self.players = players
        self.currentPlayer = None
        self.nextPlayer = None
        self.isPlaying = True
        self.hasWon = False

    def start(self):
        print("Welcome to TicTacToe! Please begin by entering your player information!")
        hasX = False
        hasO = False
        for i in range(2):
            name = input("Enter player name: ")
            if hasX:
                team = "o"
            elif hasO:
                team = "x"
            else:
                team = input("Enter player team (x or o): ")
                if team == "x":
                    hasX = True
                elif team == "o":
                    hasO = True
            player = Player(gameboard=self.gameboard, name=name, team=team)
            self.players.append(player)
            print(f"Added {player}")
        self.currentPlayer = self.players[0]
        self.nextPlayer = self.players[1]

    def turn_validator(self):
        result = None
        while result is None:
            try:
                location = input("Select a location (1-9): ")
                if int(location) not in range(1, 10):
                    raise Exception("Location is not valid.")
                elif self.gameboard.grid[location] != "-":
                    raise Exception("Location already used.")
                else:
                    result = location
            except:
                continue
        return result

    def horizontal(self):
        team = self.currentPlayer.get_team()
        grid = self.gameboard.grid
        if grid["1"] == team and grid["2"] == team and grid["3"] == team:
            return True
        elif grid["4"] == team and grid["5"] == team and grid["6"] == team:
            return True
        elif grid["7"] == team and grid["8"] == team and grid == team:
            return True
        else:
            return False

    def vertical(self):
        team = self.currentPlayer.get_team()
        grid = self.gameboard.grid
        if grid["1"] == team and grid["4"] == team and grid["7"] == team:
            return True
        elif grid["2"] == team and grid["5"] == team and grid["8"] == team:
            return True
        elif grid["3"] == team and grid["6"] == team and grid["9"] == team:
            return True
        else:
            return False

    def diagonal(self):
        team = self.currentPlayer.get_team()
        grid = self.gameboard.grid
        if grid["1"] == team and grid["5"] == team and grid["9"] == team:
            return True
        elif grid["3"] == team and grid["5"] == team and grid["7"] == team:
            return True
        else:
            return False

    def check_turn(self):
        self.take_turn()
        if self.horizontal() or self.vertical() or self.diagonal():
            print(self.currentPlayer.get_name() + " has won!")
            self.hasWon = True
            print(self.gameboard)
            self.replay()

    def take_turn(self):
        result = self.turn_validator()
        self.currentPlayer.take_turn(result)

    def switch_players(self):
        temp = self.currentPlayer
        self.currentPlayer = self.nextPlayer
        self.nextPlayer = temp

    def play(self):
        self.start()
        while self.isPlaying:
            while not self.hasWon:
                print(f"It is {self.currentPlayer.get_name()}'s turn.")
                print(self.gameboard)
                self.check_turn()
                self.switch_players()

    def replay(self):
        options = ["Y", "N"]
        answer = input("Would you like to play again? (Y/N): ").upper()
        while answer not in options:
            answer = input("Would you like to play again? (Y/N): ").upper()
        if answer == "Y":
            self.switch_players()
            self.hasWon = False
            self.gameboard.zero()
        else:
            self.isPlaying = False


if __name__ == "__main__":
    game = Game()
    game.play()
