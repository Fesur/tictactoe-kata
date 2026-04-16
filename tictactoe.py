class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]

    def make_move(self, position, player):
        if self.board[position] != " ":
            raise ValueError("Posición ocupada")
        self.board[position] = player

    def check_winner(self):
        win_positions = [
            (0,1,2), (3,4,5), (6,7,8),  # filas
            (0,3,6), (1,4,7), (2,5,8),  # columnas
            (0,4,8), (2,4,6)            # diagonales
        ]

        for a, b, c in win_positions:
            if self.board[a] == self.board[b] == self.board[c] != " ":
                return self.board[a]
        return None

    def is_draw(self):
        return " " not in self.board and self.check_winner() is None