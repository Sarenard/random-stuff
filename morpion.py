traductions = {
    "en" : {},
    "fr" : {
        "case already filled" : "case déjà remplie !",
        "player {player} just won !" : "Le joueur {player} a gagné !",
        "It's a draw !" : "Match nul !",
        "Please enter the number of the case : " : "Entrez le numéro de la case : ",
    },
    "esp" : {
        "case already filled" : "¡caso ya lleno!",
        "player {player} just won !" : "¡El jugador {player} acaba de ganar!",
        "It's a draw !" : "¡Es un empate!",
        "Please enter the number of the case : " : "Por favor ingrese el número del caso : ",
    },
}

def get_trad(language, key):
    if language in traductions:
        if key in traductions[language]:
            return traductions[language][key]
    return key

class morpion:
    def __init__(self):
        # 0 = empty, 1 = X (player 1), 2 = O (player 2)
        self.cases = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.tour = 1
    def setcase(self, nb, joueur):
        if self.cases[int(nb/3)][nb%3] == 0:
            self.cases[int(nb/3)][nb%3] = joueur
        else:
            print(get_trad(language, "case already filled"))
            import sys
            sys.exit()
        self.tour = 2 if self.tour == 1 else 1
    def getcase(self, nb):
        return self.cases[int(nb/3)][nb%3]
    def getwin(self):
        # check player 1
        if self.cases[0][2] == self.cases[1][1] == self.cases[2][0] == 1 or self.cases[0][0] == self.cases[1][1] == self.cases[2][2] == 1 or self.cases[0][2] == self.cases[1][2] == self.cases[2][2] == 1 or self.cases[0][1] == self.cases[1][1] == self.cases[2][1] == 1 or self.cases[0][0] == self.cases[1][0] == self.cases[2][0] == 1 or self.cases[2][0] == self.cases[2][1] == self.cases[2][2] == 1 or self.cases[0][0] == self.cases[0][1] == self.cases[0][2] == 1 or self.cases[1][0] == self.cases[1][1] == self.cases[1][2] == 1:
            return 1
        # check player 2
        if self.cases[0][2] == self.cases[1][1] == self.cases[2][0] == 2 or self.cases[0][0] == self.cases[1][1] == self.cases[2][2] == 2 or self.cases[0][2] == self.cases[1][2] == self.cases[2][2] == 2 or self.cases[0][1] == self.cases[1][1] == self.cases[2][1] == 2 or self.cases[0][0] == self.cases[1][0] == self.cases[2][0] == 2 or self.cases[2][0] == self.cases[2][1] == self.cases[2][2] == 2 or self.cases[0][0] == self.cases[0][1] == self.cases[0][2] == 2 or self.cases[1][0] == self.cases[1][1] == self.cases[1][2] == 2:
            return 2
        # check draw
        if self.cases[0][0] != 0 and self.cases[0][1] != 0 and self.cases[0][2] != 0 and self.cases[1][0] != 0 and self.cases[1][1] != 0 and self.cases[1][2] != 0 and self.cases[2][0] != 0 and self.cases[2][1] != 0 and self.cases[2][2] != 0:
            return 3
    def get(self, id):
        return "X" if id == 1 else "O" if id == 2 else "."
    def print_board(self):
        for i in range(3):
            print(self.get(self.cases[i][0]), self.get(self.cases[i][1]), self.get(self.cases[i][2]))
    def check_win(self):
        if self.getwin() == 1:
            print(get_trad(language, "player {player} just won !").format(player=1))
            import sys
            sys.exit()
        elif self.getwin() == 2:
            print(get_trad(language, "player {player} just won !").format(player=2))
            import sys
            sys.exit()
        elif self.getwin() == 3:
            print(get_trad(language, "It's a draw !"))
            import sys
            sys.exit()
    def play(self):
        while True:
            self.print_board()
            nb = input(get_trad(language, "Please enter the number of the case : "))
            self.setcase(int(nb), self.tour)
            self.check_win()
            
language = input("please enter your language in this list : "+str(list(traductions.keys()))+" : ")
game = morpion()
game.play()
    