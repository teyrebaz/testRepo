import random


class TicTacToe:
    def __init__(self):
        self.board = [[" "] * 3, [" "] * 3, [" "] * 3]
        self.winner = None

    def __setitem__(self, coord, symbol):
        self.board[coord[0]][coord[1]] = symbol

    def __getitem__(self, coord):
        return self.board[coord[0]][coord[1]]

    @staticmethod
    def check_row(symbol, row):
        return all(map(lambda x: x == symbol, row))

    def check_winner(self, symbol):
        for row in self.board:
            if self.check_row(symbol, row):
                self.winner = symbol
                return True
        for row in zip(*self.board):
            if self.check_row(symbol, row):
                self.winner = symbol
                return True
        diagonal1 = [self.board[i][i] for i in range(3)]
        diagonal2 = [self.board[i][-i - 1] for i in range(3)]

        for row in [diagonal1, diagonal2]:
            if self.check_row(symbol, row):
                self.winner = symbol
                return True
        return False

    def print_board(self):
        print("---------")
        for row in self.board:
            print("| {0} {1} {2} |".format(row[0], row[1], row[2]))
        print("---------")


class User:
    def __init__(self, name, sign):
        self.name = name
        self.sign = sign

    @staticmethod
    def easy_move(board):
        lst = []
        for i in board:
            for j in i:
                if j == " ":
                    lst.append([board.index(i), i.index(j)])
        return random.choice(lst)

    def make_move(self, board):
        if not self.is_move(board):
            return None
        if self.name == "easy":
            print('Making move level "easy"')
            return self.easy_move(board)
        if self.name == "medium":
            rows = self.all_rows(board)
            for row in rows:
                if self.sign == "X":
                    if row.count("X") == 2 and " " in row:
                        print('Making move level "medium"')
                        return [rows.index(row), row.index(" ")]
                    elif row.count("O") == 2 and " " in row:
                        print('Making move level "medium"')
                        return [rows.index(row), row.index(" ")]
                    else:
                        print('Making move level "medium"')
                        return self.easy_move(board)
                if self.sign == "O":
                    if row.count("O") == 2 and " " in row:
                        print('Making move level "medium"')
                        return [rows.index(row), row.index(" ")]
                    elif row.count("X") == 2 and " " in row:
                        print('Making move level "medium"')
                        return [rows.index(row), row.index(" ")]
                    else:
                        print('Making move level "medium"')
                        return self.easy_move(board)
        if self.name == "user":
            while True:
                if not self.is_move(board):
                    return None
                coordinates = input("Enter the coordinates: >")
                if coordinates == "exit":
                    return None
                coordinates = coordinates.split()
                if len(coordinates) == 0:
                    continue
                str_coord = "".join(coordinates)
                try:
                    coordinates = [int(i) for i in coordinates]
                except ValueError:
                    print("You should enter numbers!")
                    continue
                if not (0 < coordinates[0] <= 3 and 0 < coordinates[1] <= 3):
                    print("Coordinates should be from 1 to 3!")
                    continue
                index = self.convert_coord(str_coord)
                if board[index[0]][index[1]] != " ":
                    print("This cell is occupied! Choose another one!")
                    continue
                else:
                    return index

    @staticmethod
    def all_rows(board2):
        board = board2.copy()
        for row in zip(*board):
            board.append(row)
        board.append([board[0][0], board[1][1], board[2][2]])
        board.append([board[0][2], board[1][1], board[2][0]])
        return board

    @staticmethod
    def is_move(board):
        for i in board:
            for j in i:
                if j == " ":
                    return True
        return False

    @staticmethod
    def convert_coord(crd):  # converts given coordinates to list index
        coord_dict = {"13": [0, 0], "23": [0, 1], "33": [0, 2],
                      "12": [1, 0], "22": [1, 1], "32": [1, 2],
                      "11": [2, 0], "21": [2, 1], "31": [2, 2]}
        return coord_dict[crd]


while True:
    input_lst = input("Input command: > ").split()
    if len(input_lst) != 3:
        print("Bad parameters!")
        continue
    elif input_lst[0] == "exit":
        break
    else:
        game = TicTacToe()
        userX = User(input_lst[1], "X")
        userO = User(input_lst[2], "O")
        game.print_board()
        while True:
            index_x = userX.make_move(game.board)
            if index_x is None:
                print("Draw")
                break
            game[index_x] = userX.sign
            game.print_board()
            if game.check_winner(userX.sign):
                print(f"{game.winner} wins")
                break
            index_o = userO.make_move(game.board)
            if index_o is None:
                print("Draw")
                break
            game[index_o] = userO.sign
            game.print_board()
            if game.check_winner(userO.sign):
                print(f"{game.winner} wins")
                break
        break
