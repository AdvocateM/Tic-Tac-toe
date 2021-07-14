# *************************Global********************
# Board
Board = ["",
"_", "_", "_",
"_", "_", "_",
"_", "_", "_"] # 0 is excludeted. 
#

#If Game is active
game_still_on = True
#


# check the current player
current_player = "X"

#who is the legend
winner = None


# Global end here
#Display
def Display_board():
  print(f"{Board[1]} | {Board[2]} | {Board[3]}")
  print(f"{Board[4]} | {Board[5]} | {Board[6]}")
  print(f"{Board[7]} | {Board[8]} | {Board[9]}")



#play Tic Tac toe
def Play_game():

  #Display initial Board
  Display_board()

  # while game still open
  while game_still_on:

      #handle player
      hundle_player(current_player)

      check_if_game_over()

      flip_player()
  
  # Game ends here
  if winner == "X" or winner == "O":
    print(f"{winner} Won.")

  elif winner == None:
    print("Tie.")
  

# check if game is over
def check_if_game_over():
  check_if_win()
  check_if_tie()
  ...

def check_if_win():

  #global access varible
  global winner
  # check rows
  row_winner = rows()
  
  # check columns
  colum_winner = colums()

  #check diagonals
  diagonal_winner = diagonals()


  if row_winner:
    winner = row_winner
    ...
  elif colum_winner:
    winner = colum_winner
    ...
  elif diagonal_winner:
    winner = diagonal_winner
    ...
  else:
    winner = None

#check rows
def rows():
  global game_still_on

  # check matches
  row_1 = Board[1] == Board[2] == Board[3] != "_"
  row_2 = Board[4] == Board[5] == Board[6] != "_"
  row_3 = Board[7] == Board[8] == Board[9] != "_"

  # If any match
  if row_1 or row_2 or row_3:
    game_still_on = False

  # Return the winner X or O
  if row_1:
    return Board[1]
  
  elif row_2:
    return Board[4]
  
  elif row_3:
    return Board[7]
  return
  

# check colums
def colums():
  global game_still_on

  # check matches
  colum_1 = Board[1] == Board[4] == Board[7] != "_"
  colum_2 = Board[2] == Board[5] == Board[8] != "_"
  colum_3 = Board[3] == Board[6] == Board[9] != "_"

  # If any match
  if colum_1 or colum_2 or colum_3:
    game_still_on = False

  # Return the winner X or O
  if colum_1:
    return Board[1]
  
  elif colum_2:
    return Board[2]
  
  elif colum_3:
    return Board[3]
  return
  

#check diagonal
def diagonals():
  global game_still_on

  # check matches
  diagonal_1 = Board[1] == Board[5] == Board[3] != "_"
  diagonal_2 = Board[7] == Board[5] == Board[8] != "_"

  # If any match
  if diagonal_1 or diagonal_2:
    game_still_on = False

  # Return the winner X or O
  if diagonal_1:
    return Board[1]
  
  elif diagonal_2:
    return Board[7]
  return


#check Tie
def check_if_tie():
  global game_still_on

  if "_" not in Board:
    game_still_on = False

  return 

# Flip
def flip_player():

  global current_player

  if current_player == "X":
    current_player = "O"
  elif current_player == "O":
    current_player = "X"
  


def hundle_player(player):

  print(f"{player}'s turn.'")

  position = int(input("Enter a number from 1 to 9: "))

  valid = False
  while not valid:

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
      position = int(input("Oops that's an invalid number. try 1 to 9: "))

    if Board[position] == "_":
      valid = True
    else:
      print("You can't go there.")
      position = int(input("try emty space from 1 to 9: "))
      
  Board[position] = player
  Display_board()
  ...

Play_game()
