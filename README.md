# Tic Tac Toe Game

This is a simple implementation of the classic Tic Tac Toe game in Python. The game is played on a 3x3 grid, and the goal is to get three of your own marks (either 'O') in a row, horizontally, vertically, or diagonally.

## Demo

[Play the game on Replit](https://replit.com/@abenteuerzeit/tic-tac-toe)

- Click on the link
- Click the play button
- Enter a number to select a position!
- ???
- Win!

https://github.com/abenteuerzeit/tic-tac-toe/assets/98088666/098e5bbf-0c3c-41ad-aab5-78265aea7159

## Features

- Play against the computer
- Random computer starting position
- Configurable game settings

## Requirements

- Python 3.x

## Usage

1. Clone the repository:

```bash
git clone (https://github.com/abenteuerzeit/tic-tac-toe.git
```

2. Navigate to the cloned repository:

```bash
cd tic-tac-toe
```

3. Run the game:

```bash
python start.py
```

## Configuration

You can customize the game by modifying the `CONFIG` dictionary in `tictactoe.py`. Here are the available settings:

- `BOARD_SIZE`: The size of the game board (default is 3 for a 3x3 board).
- `MIN_MOVE`: The minimum valid move number (default is 1).
- `MAX_MOVE`: The maximum valid move number (default is 9).
- `SIGNS`: The signs used by the players (default is ['O', 'X']).
- `BAD_MOVE_MSG`: The message displayed when a player makes an invalid move.
- `FIELD_OCCUPIED_MSG`: The message displayed when a player tries to move to an occupied field.
- `YOU_WON_MSG`: The message displayed when the human player wins.
- `I_WON_MSG`: The message displayed when the computer wins.
- `TIE_MSG`: The message displayed when the game is a tie.
- `COMPUTER`: The name used for the computer player.
- `HUMAN`: The name used for the human player.

## Contributing

Just to let you know, pull requests are welcome. For major changes, please open an issue first to discuss what you want to change.
