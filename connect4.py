'''
Name: Abdulrehman Nakhuda
Date: November 22, 2022
Description:
    Connect 4 - Player vs AI

    The main goal of this project is to develop the game Connect 4
where a player can compete against an AI on a 6x7 grid. The objective is
to be the first to connect four pieces either vertically, horizontally or
diagonally. The game has a user interface that allows players to input the
column where they want to drop their piece and view the state of the board.
The AI moves are made on a random basis. To represent the game board we use
a list of lists, where each element in the list corresponds to a row and
each element in the list represents a column. There are functions implemented
to check if either the player or AI has won, with "X" representing the players
victory, "O" representing the AIs victory and an empty string ("") signifying
that no one has won based on the state of the board.

    Another function enables players to drop their pieces into columns and updates
the board accordingly. Within this move making function for both AI and player
turns there is logic in place that verifies if its possible for a player to
drop their piece in their chosen column. This logic considers both the state
of the board and whether or not that particular column's available for placement.
Additionally there is an added feature called "Hall of Fame" where players can
add their names if they manage to defeat the AI. Each time you run the code this
Hall of Fame display appears first. The program verifies if a file called
"cps109_a1_output.txt" is present. If it is not found it notifies the players
that nobody has ever defeated the AI previously. If the file exists, the code
prints "Hall of Fame:" followed by the names of players who beat the AI and
updates the text file with the newly added winner's name.
'''

import random
import os.path


def winner(board):
  """This function accepts the Connect Four board as a parameter.
  If there is no winner, the function will return the empty string "".
  If the user has won, it will return "X", and if the computer has
  won it will return "O"."""
  # Check horizontals for winner
  for col in range(0, 4):
    for row in range(6):
      if (board[row][col] == board[row][col + 1] == board[row][col + 2] ==
          board[row][col + 3]) and (board[row][col] != " "):
        return board[row][col]
  # Check verticals for winner
  for col in range(7):
    for row in range(0, 3):
      if (board[row][col] == board[row + 1][col] == board[row + 2][col] ==
          board[row + 3][col]) and (board[row][col] != " "):
        return board[row][col]
  # Check diagonals (negative slope) for winner
  for col in range(0, 4):
    for row in range(0, 3):
      if (board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2]
          == board[row + 3][col + 3]) and (board[row][col] != " "):
        return board[row][col]
  # Check diagonals (positive slope) for winner
  for col in range(3, 7):
    for row in range(0, 3):
      if (board[row][col] == board[row + 1][col - 1] == board[row + 2][col - 2]
          == board[row + 3][col - 3]) and (board[row][col] != " "):
        return board[row][col]
  # No winner
  return ""


def display_board(board):
  """This function accepts the Connect Four board as a parameter.
    It will print the Connect Four board grid (using ASCII characters)
    and show the positions of any X's and O's.  It also displays
    the column numbers on top of the board to help the user figure out
    the coordinates of their next move.
    This function does not return anything."""

  for col in range(len(board[0])):
    print("   " + str(col), end="")
  print()

  for row in range(len(board) - 1):
    print('', "  " + (" | ".join(board[row])))
    print('', " ---" + "+---" * (len(board[row]) - 1))
  print('', "  " + (" | ".join(board[row + 1])))
  print()


def make_user_move(board):
  """This function accepts the Connect Four board as a parameter.
  It will ask the user for a column to drop their next "X".  If the column
  given is valid (within range), and there is a free cell in the column, then it will place an "X" in the next available cell within the column."""
  #row variable creation
  row = 5

  #user input for the column
  col = int(input("What column would you like to drop the disc in? (0-6):"))

  #flag variable
  valid_move = True

  #Checking if the user input is valid
  while valid_move:
    if row == -1:
      while board[row][col] != " ":
        col = int(input("Sorry, invalid square. Please try again:"))
    if (0 <= col <= 6) and (board[row][col] == " "):
      board[row][col] = "X"
      return board[row][col]
      row -= 1
      valid_move = False
    elif (0 <= col <= 6) and (board[row][col] != " "):
      row -= 1
    #If the user input is invalid
    else:
      col = int(input("Sorry, invalid square. Please try again:"))


def make_computer_move(board):
  """This function accepts the Connect Four board as a parameter.
  It will randomly pick a column value between 0 and 7.
  If that square is not already occupied it will place an "O"
  in that square.  Otherwise, another random row and column
  will be generated."""
  #row variable creation
  row = 5

  #Computer input for column
  col = random.randint(0, 6)

  #flag variable
  valid_move = True

  #checking if the computer input is valid
  while valid_move:
    if row == -1:
      while board[row][col] != " ":
        col = random.randint(0, 6)
    if (0 <= col <= 6) and (board[row][col] == " "):
      board[row][col] = "O"
      return board[row][col]
      row -= 1
      valid_move = False
    elif (0 <= col <= 6) and (board[row][col] != " "):
      row -= 1


def main():
  """Our Main Game Loop:"""
  #Check if there such a file exists
  instructions=open("Connect_4_How_To.txt","r")
  for i in instructions:
      print(i)
  if os.path.exists("cps109_a1_output.txt"):
    print("Hall of Fame:\n")
    read = open("cps109_a1_output.txt", "r")
    num = 0
    #Displaying the scoreboard
    for i in (read):
      num += 1
      print(str(num) + ") " + i)
  else:
    print("No Human Has Ever Beat Me..mwah-ha-ha-ha!")
  #Create the first board - filled with empty strings " ".
  board = []
  for row in range(1, 7):
    board.append([" "] * 7)
  display_board(board)

  #Number of open cells
  cells = 6 * 7

  #flag variable
  holder = True

  #checking if user input is valid
  response = ["Y", "y", "N", "n"]
  while holder == True:
    first = input("Would you like to go first?[Y/N]")
    if first in response[:2]:
      while holder:
        if not winner(board) and cells > 0:
          cells -= 1
          make_user_move(board)
          if not winner(board) and cells > 0:
            make_computer_move(board)
          display_board(board)
        else:
          holder = False

    elif first in response[2:]:
      while holder:
        if not winner(board) and cells > 0:
          cells -= 1
          make_computer_move(board)
          display_board(board)
          make_user_move(board)
          if winner(board) and cells > 0:
            display_board(board)
        else:
          holder = False
    #if the user input is invalid
    else:
      print("Invalid Entry!")

  #Creating and opening the Hall of Fame text file
  hallOfFame = open("cps109_a1_output.txt", "a")

  #Checking the winner
  if (winner(board) == 'X'):
    print("Y O U   W O N !")
    name = input("Enter your name:")
    hallOfFame.write(name)
    hallOfFame.write("\n")
    hallOfFame.close()

  elif (winner(board) == 'O'):
    print("Y O U   L O S T!")

  else:
    print("S T A L E M A T E !")
  print("\n*** GAME OVER ***\n")


# Start the game!
main()
