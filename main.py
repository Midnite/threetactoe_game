import pygame
from sys import exit
from threetactoe.game import Game


def main():
    game_instance = Game()

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            game_instance.handle_events(event)


main()
