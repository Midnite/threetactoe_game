import unittest
import pygame
from pygame.locals import MOUSEBUTTONDOWN
from threetactoe.game import Game
import threetactoe.config as config


class TestGame(unittest.TestCase):
    def setUp(self):
        # Create a new Game instance before each test
        self.game = Game()

    def test_reset_game(self):
        # Test if game state is correctly reset
        self.game.reset_game()
        self.assertEqual(self.game.current_player, 0)
        self.assertEqual(self.game.game_over, False)
        self.assertEqual(self.game.board, [
                         [' ' for _ in range(4)] for _ in range(4)])

    def test_is_valid(self):
        # Test if game correctly identifies valid and invalid moves
        self.game.board[0][0] = 'X'
        self.assertEqual(self.game.is_valid(0, 0), False)
        self.assertEqual(self.game.is_valid(0, 1), True)

    def test_mark_cell(self):
        # Test if game correctly marks a cell
        self.game.mark_cell(0, 0, 'X')
        self.assertEqual(self.game.board[0][0], 'X')

    def test_check_win_rows(self):
        # Test if game correctly identifies a win in a row
        self.game.board[0][0] = 'X'
        self.game.board[0][1] = 'X'
        self.game.board[0][2] = 'X'
        self.assertEqual(self.game.check_win('X'), True)
        self.assertEqual(self.game.check_win('O'), False)

    def test_check_win_columns(self):
        # Test if game correctly identifies a win in a column
        self.game.board[0][0] = 'X'
        self.game.board[1][0] = 'X'
        self.game.board[2][0] = 'X'
        self.assertEqual(self.game.check_win('X'), True)

    def test_check_win_diagonals(self):
        # Test if game correctly identifies a win in a diagonal
        self.game.board[0][0] = 'X'
        self.game.board[1][1] = 'X'
        self.game.board[2][2] = 'X'
        self.assertEqual(self.game.check_win('X'), True)

    def test_check_win_no_win(self):
        # Test if game correctly identifies when there is no win
        self.game.board[0][0] = 'X'
        self.game.board[0][1] = 'X'
        self.game.board[0][2] = 'O'
        self.assertEqual(self.game.check_win('X'), False)

    def test_is_board_full(self):
        # Test if game correctly identifies when the board is full
        self.game.board = [['X' for _ in range(4)] for _ in range(4)]
        self.assertEqual(self.game.is_board_full(), True)

        self.game.board[0][0] = ' '
        self.assertEqual(self.game.is_board_full(), False)

    def test_handle_events_on_board(self):
        # Test if game correctly handles MOUSEBUTTONDOWN events on the board
        self.game.handle_events(
            pygame.event.Event(MOUSEBUTTONDOWN, pos=(0, 0)))
        self.assertEqual(self.game.board[0][0], 'X')

        self.game.handle_events(pygame.event.Event(
            MOUSEBUTTONDOWN, pos=(0, config.CELL_SIZE)))
        self.assertEqual(self.game.board[1][0], 'O')

        self.game.handle_events(pygame.event.Event(
            MOUSEBUTTONDOWN, pos=(0, 2 * config.CELL_SIZE)))
        self.assertEqual(self.game.board[2][0], 'Square')

    def test_handle_events_off_board(self):
        # Test if game correctly ignores MOUSEBUTTONDOWN events off the board
        self.game.handle_events(pygame.event.Event(
            MOUSEBUTTONDOWN, pos=(0, config.BOARD_HEIGHT)))
        self.assertEqual(self.game.board, [
                         [' ' for _ in range(4)] for _ in range(4)])


if __name__ == "__main__":
    unittest.main()
