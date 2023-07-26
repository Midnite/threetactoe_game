import pygame
from .config import *
from .render import Renderer


class Game:
    def __init__(self):
        self.players = ["X", "O", "Square"]
        self.current_player = 0
        self.board = None
        self.game_over = False
        self.button = pygame.Rect(
            WIDTH // 2 - 50, BOARD_HEIGHT + STATUS_BAR_HEIGHT - 40, 100, 30)
        self.renderer = Renderer(self.button)
        self.reset_game()

    def reset_game(self):
        self.board = [[' ' for _ in range(4)] for _ in range(4)]
        self.current_player = 0
        self.game_over = False
        self.renderer.reset_screen()
        self.renderer.draw_lines()
        self.renderer.render_status_text("Welcome to Threetac Toe!")

    def is_valid(self, row, col):
        return 0 <= row < 4 and 0 <= col < 4 and self.board[row][col] == ' '

    def mark_cell(self, row, col, player):
        self.board[row][col] = player

    def check_win(self, player):
        # Check rows
        for row in range(4):
            for col in range(2):
                if all(self.board[row][col+i] == player for i in range(3)):
                    return True

        # Check columns
        for col in range(4):
            for row in range(2):
                if all(self.board[row+i][col] == player for i in range(3)):
                    return True

        # Check diagonals
        for row in range(2):
            for col in range(2):
                if all(self.board[row+i][col+i] == player for i in range(3)):
                    return True

        # Check reverse diagonals
        for row in range(2):
            for col in range(2, 4):
                if all(self.board[row+i][col-i] == player for i in range(3)):
                    return True

        return False

    def is_board_full(self):
        for row in range(4):
            for col in range(4):
                if self.board[row][col] == ' ':
                    return False
        return True

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = event.pos
            clicked_row = mouseY // CELL_SIZE
            clicked_col = mouseX // CELL_SIZE

            if self.game_over:
                if self.button.collidepoint(pygame.mouse.get_pos()):
                    self.reset_game()
            else:
                if clicked_row < 5 and clicked_col < 5:
                    if self.is_valid(clicked_row, clicked_col):
                        self.mark_cell(clicked_row, clicked_col,
                                       self.players[self.current_player])
                        if self.check_win(self.players[self.current_player]):
                            self.game_over = True
                            self.renderer.render_status_text(
                                f"Player {self.players[self.current_player]} wins!", True)
                            self.renderer.draw_button()
                        elif self.is_board_full():
                            self.game_over = True
                            self.renderer.render_status_text(
                                "Everyone lost!", True)
                            self.renderer.draw_button()
                        else:
                            self.current_player = (
                                self.current_player + 1) % len(self.players)
                            self.renderer.render_status_text(
                                f"Player {self.players[self.current_player]}'s turn")
                    else:
                        self.renderer.render_status_text(
                            "Can't do that, try another cell!")

        self.renderer.draw_figures(self.board)
        self.renderer.update_screen()
