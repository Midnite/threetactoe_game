import pygame
from .config import *

pygame.init()
pygame.display.set_caption("Threetac Toe")
screen = pygame.display.set_mode((WIDTH, BOARD_HEIGHT + STATUS_BAR_HEIGHT))
screen.fill(BG_COLOR)

font = pygame.font.SysFont("Arial", 20)
button_font = pygame.font.SysFont("Arial", 14)


class Renderer:
    def __init__(self, button):
        self.button = button

    def reset_screen(self):
        screen.fill(BG_COLOR)

    # Draw the board
    def draw_lines(self):
        for i in range(1, 4):
            pygame.draw.line(screen, LINE_COLOR, (0, i * CELL_SIZE),
                             (BOARD_HEIGHT, i * CELL_SIZE), LINE_WIDTH)
        for i in range(1, 4):
            pygame.draw.line(screen, LINE_COLOR, (i * CELL_SIZE, 0),
                             (i * CELL_SIZE, BOARD_HEIGHT), LINE_WIDTH)

    # Draw player symbols
    def draw_figures(self, board):
        for row in range(4):
            for col in range(4):
                if board[row][col] != ' ':
                    if board[row][col] == 'X':
                        pygame.draw.line(screen, CROSS_COLOR, (col * CELL_SIZE + SPACE, row * CELL_SIZE + CELL_SIZE -
                                         SPACE), (col * CELL_SIZE + CELL_SIZE - SPACE, row * CELL_SIZE + SPACE), CROSS_WIDTH)
                        pygame.draw.line(screen, CROSS_COLOR, (col * CELL_SIZE + SPACE, row * CELL_SIZE + SPACE),
                                         (col * CELL_SIZE + CELL_SIZE - SPACE, row * CELL_SIZE + CELL_SIZE - SPACE), CROSS_WIDTH)
                    elif board[row][col] == 'O':
                        pygame.draw.circle(screen, CIRCLE_COLOR, (col * CELL_SIZE + CELL_SIZE //
                                           2, row * CELL_SIZE + CELL_SIZE // 2), CIRCLE_RADIUS, CIRCLE_WIDTH)
                    elif board[row][col] == 'Square':
                        square_half_size = SQUARE_SIZE // 2
                        square_center_x = col * CELL_SIZE + CELL_SIZE // 2
                        square_center_y = row * CELL_SIZE + CELL_SIZE // 2
                        pygame.draw.rect(screen, SQUARE_COLOR, pygame.Rect(
                            square_center_x - square_half_size, square_center_y - square_half_size, SQUARE_SIZE, SQUARE_SIZE))

    def render_status_text(self, text, draw_button=False):
        # Draw status bar
        pygame.draw.rect(screen, STATUS_BAR_COLOR, pygame.Rect(
            0, BOARD_HEIGHT, WIDTH, STATUS_BAR_HEIGHT))
        status_surface = font.render(text, True, FONT_COLOR)

        # Calculate y-coordinate for blitting the status text
        y_coord = BOARD_HEIGHT + 10 if draw_button else BOARD_HEIGHT + 25

        # Blit status text onto the screen
        screen.blit(status_surface, (WIDTH // 2 -
                    status_surface.get_width() // 2, y_coord))

    def draw_button(self, text="Go again?"):
        pygame.draw.rect(screen, BUTTON_COLOR, self.button)
        button_surface = button_font.render(text, True, BUTTON_FONT_COLOR)
        button_rect = button_surface.get_rect(center=self.button.center)
        screen.blit(button_surface, button_rect)

    def update_screen(self):
        pygame.display.update()
