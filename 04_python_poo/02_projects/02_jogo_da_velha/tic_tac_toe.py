import random
import os


class TicTacToe:
    def __init__(self):
        self.reset()

    def print_board(self):
        print("")
        print(" " + self.board[0][0] + " | " +
              self.board[0][1] + " | " + self.board[0][2])
        print("___________")
        print(" " + self.board[1][0] + " | " +
              self.board[1][1] + " | " + self.board[1][2])
        print("___________")
        print(" " + self.board[2][0] + " | " +
              self.board[2][1] + " | " + self.board[2][2])

    def reset(self):
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.done = ""

    def check_win_or_draw(self):
        dict_win = {}
        for x in ['X', 'O']:
            # Condição Horizontal
            dict_win[x] = (self.board[0][0] == self.board[0][1] == self.board[0][2])
            dict_win[x] = (self.board[1][0] == self.board[1][1] == self.board[1][2]) or dict_win[x]
            dict_win[x] = (self.board[2][0] == self.board[2][1] == self.board[2][2]) or dict_win[x]
            # Condição Vertical
            dict_win[x] = (self.board[0][0] == self.board[1][0] == self.board[2][0])
            dict_win[x] = (self.board[0][1] == self.board[1][1] == self.board[2][1]) or dict_win[x]
            dict_win[x] = (self.board[0][2] == self.board[1][2] == self.board[2][2]) or dict_win[x]
            # Condição Diagonal
            dict_win[x] = (self.board[0][0] == self.board[1][1] == self.board[2][2]) or dict_win[x]
            dict_win[x] = (self.board[2][0] == self.board[1][1] == self.board[0][2]) or dict_win[x]

        if dict_win['X']:
            self.done = 'x'
            print('X venceu')
            return
        elif dict_win['O']:
            self.done = 'o'
            print('O venceu')
            return
        c = 0

        for i in range(3):
            for j in range(3):
                if self.board[i][j] != " ":
                    c+1
                    break

        if c == 0:
            self.done = 'd'
            print('Empate')
            return

    def get_player_move(self):
        invalid_mode = True
        while invalid_mode:
            try:
                print('Digite a linha do seu próximo lance:')
                x = int(input())
                print('Digite a columna do seu próximo lance:')
                y = int(input())
                if x > 2 or x < 0 or y > 2 or y < 0:
                    print('Coordenadas inválidas')
                if self.board[x][y] != " ":
                    print('Posição já preenchida')
                    continue
            except Exception as e:
                print(e)
                continue
            invalid_mode = False
            self.board[x][y] = 'X'

    def make_move(self):
        list_moves = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    list_moves.append((i, j))
            if len(list_moves) > 0:
                x, y = random.choice(list_moves)
                self.board[x][y] = 'O'


self = TicTacToe()
self.print_board()
