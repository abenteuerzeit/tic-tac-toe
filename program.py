import os
from random import randrange


# Global configuration settings
CONFIG = {
    "BOARD_SIZE": 3,
    "MIN_MOVE": 1,
    "MAX_MOVE": 9,
    "SIGNS": ['O', 'X'],
    "BAD_MOVE_MSG": "Bad move - repeat your input!",
    "FIELD_OCCUPIED_MSG": "Field already occupied - repeat your input!",
    "YOU_WON_MSG": "You won!",
    "I_WON_MSG": "I won",
    "TIE_MSG": "Tie!",
    "COMPUTER": "computer",
    "HUMAN": "human"
}


def display_board(board):
    print("+-------" * CONFIG["BOARD_SIZE"],"+",sep="")
    for row in range(CONFIG["BOARD_SIZE"]):
        print("|       " * CONFIG["BOARD_SIZE"],"|",sep="")
        for column in range(CONFIG["BOARD_SIZE"]):
            print("|   " + str(board[row][column]) + "   ",end="")
        print("|")
        print("|       " * CONFIG["BOARD_SIZE"],"|",sep="")
        print("+-------" * CONFIG["BOARD_SIZE"],"+",sep="")


def enter_human_move(board):
    is_valid_move = False
    while not is_valid_move:
        move = input("Enter your move: ")
        is_valid_move = len(move) == 1 and move >= str(CONFIG["MIN_MOVE"]) and move <= str(CONFIG["MAX_MOVE"])
        if not is_valid_move:
            print(CONFIG["BAD_MOVE_MSG"])
            continue
        move = int(move) - 1
        row = move // CONFIG["BOARD_SIZE"]
        column = move % CONFIG["BOARD_SIZE"]
        sign = board[row][column]
        is_valid_move = sign not in CONFIG["SIGNS"]
        if not is_valid_move:
            print(CONFIG["FIELD_OCCUPIED_MSG"])
            continue
    board[row][column] = CONFIG["SIGNS"][0]


def get_list_of_free_fields(board):
    free_fields = []
    for row in range(CONFIG["BOARD_SIZE"]):
        for column in range(CONFIG["BOARD_SIZE"]):
            if board[row][column] not in CONFIG["SIGNS"]:
                free_fields.append((row,column))
    return free_fields


def check_victory_for(board, sgn):
    if sgn == CONFIG["SIGNS"][1]:
        player = CONFIG["COMPUTER"]
    elif sgn == CONFIG["SIGNS"][0]:
        player = CONFIG["HUMAN"]
    else:
        player = None
    is_diagonal1 = is_diagonal2 = True
    for rc in range(CONFIG["BOARD_SIZE"]):
        if board[rc][0] == sgn and board[rc][1] == sgn and board[rc][2] == sgn:
            return player
        if board[0][rc] == sgn and board[1][rc] == sgn and board[2][rc] == sgn:
            return player
        if board[rc][rc] != sgn:
            is_diagonal1 = False
        if board[CONFIG["BOARD_SIZE"] - 1 - rc][CONFIG["BOARD_SIZE"] - 1 - rc] != sgn:
            is_diagonal2 = False
    if is_diagonal1 or is_diagonal2:
        return player
    return None


def draw_computer_move(board):
    free_fields = get_list_of_free_fields(board)
    num_free_fields = len(free_fields)
    if num_free_fields > 0:
        this = randrange(num_free_fields)
        row, col = free_fields[this]
        board[row][col] = CONFIG["SIGNS"][1]


def play_game():
  board = [ [CONFIG["BOARD_SIZE"] * j + i + 1 for i in range(CONFIG["BOARD_SIZE"])] for j in range(CONFIG["BOARD_SIZE"]) ]
  board[randrange(0,CONFIG["BOARD_SIZE"])][randrange(0,CONFIG["BOARD_SIZE"])] = CONFIG["SIGNS"][1]
  free_fields = get_list_of_free_fields(board)
  is_human_turn = True
  while len(free_fields):
      display_board(board)
      if is_human_turn:
          enter_human_move(board)
          victor = check_victory_for(board,CONFIG["SIGNS"][0])
      else:    
          draw_computer_move(board)
          victor = check_victory_for(board,CONFIG["SIGNS"][1])
      os.system('cls' if os.name == 'nt' else 'clear')
      if victor != None:
          break
      is_human_turn = not is_human_turn        
      free_fields = get_list_of_free_fields(board)
  
  display_board(board)
  if victor == CONFIG["HUMAN"]:
      print(CONFIG["YOU_WON_MSG"])
  elif victor == CONFIG["COMPUTER"]:
      print(CONFIG["I_WON_MSG"])
  else:
      print(CONFIG["TIE_MSG"])


if __name__ == "__main__":
  play_game()
