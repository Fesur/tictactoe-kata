import unittest
from tictactoe import TicTacToe

class TestTicTacToe(unittest.TestCase):

    def test_move(self):
        game = TicTacToe()
        game.make_move(0, "X")
        self.assertEqual(game.board[0], "X")

    def test_invalid_move(self):
        game = TicTacToe()
        game.make_move(0, "X")
        with self.assertRaises(ValueError):
            game.make_move(0, "O")

    def test_row_win(self):
        game = TicTacToe()
        game.board = ["X", "X", "X", " ", " ", " ", " ", " ", " "]
        self.assertEqual(game.check_winner(), "X")

    def test_column_win(self):
        game = TicTacToe()
        game.board = ["O", " ", " ", "O", " ", " ", "O", " ", " "]
        self.assertEqual(game.check_winner(), "O")

    def test_diagonal_win(self):
        game = TicTacToe()
        game.board = ["X", " ", " ", " ", "X", " ", " ", " ", "X"]
        self.assertEqual(game.check_winner(), "X")

    def test_draw(self):
        game = TicTacToe()
        game.board = ["X","O","X","X","O","O","O","X","X"]
        self.assertTrue(game.is_draw())

    def test_no_winner(self):
        game = TicTacToe()
        self.assertIsNone(game.check_winner())

if __name__ == "__main__":
    unittest.main()