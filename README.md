# Threetac Toe

Threetac Toe is a slightly more complex variation of the classic Tic Tac Toe game. Instead of the traditional two players, Threetac Toe involves three different players and a 4x4 game board, adding an extra layer of strategy and fun to the old classic. You still need three matching symbols to win, but going against two opponents ups the excitement for all involved.

## Description

![Welcome game screen](/assets/game_screen_1.png)
![Active game screen](/assets/game_screen_2.png)
![Winner game screen](/assets/game_screen_3.png)

This project is built using Python and the [Pygame library](https://www.pygame.org/) for rendering the UI. The goal of each player (X, O and Square) is to get three of their own marks in a row, either horizontally, vertically, or diagonally, while taking turns placing symbols.

Building Threetac Toe presented some minor challenges for its developer. During the first implementation, when one symbol in a diagonal winning combination was on the bottom row of the grid, the win condition checking did not work correctly and simply ignored the victory. 

The first iteration also featured a 5x5 grid, which made it virtually impossible for the starting player not to win, damaging the user experience quite a bit. I've addressed these issues and the game is now perfect.

Pygame is a brilliant library for developing simple Python games with minimal hassle, it's also not intended for creating complex graphical user interfaces, which is absolutely reflected in the way Threetac Toe looks.

## Installation

To run Threetac Toe:

1. Clone this repository:

```bash
git clone https://github.com/Midnite/threetactoe_game.git
```

2. Navigate to the project directory:

```bash
cd threetactoe_game
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

To start a game of Threetac Toe, run the following command from the project's root directory:

```bash
python main.py
```

The game board will appear, and players can take turns clicking on the board to place their marks. The current player's turn and game results will be displayed in the status bar below the game board.

## Testing

Python's built-in `unittest` module is used for tests. To run the test suite, use the following command from the project's root directory:

```bash
python -m unittest discover tests
```

## License

This project is licensed under the MIT License. It exists for fun and for the sake of doing Python.
