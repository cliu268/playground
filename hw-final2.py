# Thursday Class Code! Ryan's Python beginner class final project: battleship game
import random

boardcomputer = []
boardperson = []
opensquaresleft = []
def placeship(board, size, orientation):
  #Orientation is either going to be true or false
  #True refers to the ship being horizontal
  #False refers to the ship being vertical
  #Location is the set of coordinates [row, column] that tells us where the
  #captain of the ship is.
  location = []
  if (not orientation):
    location.append(random.randrange(0, 9-size))
    location.append(random.randrange(0,7))
    for i in range(location[0], location[0] + size):
      board[i][location[1]] = 1
  else:
    location.append(random.randrange(0, 7))
    location.append(random.randrange(0, 9-size))
    for i in range(location[1], location[1] + size):
      board[location[0]][i] = 1
  
def createboards():
  global boardcomputer
  global boardperson

  for i in range(8):
    fillerlist = []
    for j in range(8):
      fillerlist.append(0)
    boardcomputer.append(fillerlist.copy())
    boardperson.append(fillerlist.copy())
  for i in range(8):
    for j in range(8):
      opensquaresleft.append([i, j])
  placeship(boardcomputer, 4, True)
  placeship(boardperson, 4, True)
def printlist(A):
  returnstring = ""
  for i in A:
    returnstring = returnstring + str(i) + " "
  print(returnstring)
def printboard(board):
  for i in board:
    printlist(i)
  print()
def changelist(A):
  returnlist = []
  for i in A:
    if i == 0 or i == 1:
      returnlist.append("_")
    elif i == 2:
      returnlist.append("O")
    else:
      returnlist.append("X")
  return returnlist

def specialprintboard(board):
  #I'm going to print out a normal board using _ as unmarked spaces
  #X being marked spaces that have a ship on it
  #O
  for i in board:
    printlist(changelist(i))
  print()

def gameover(board):
  #This returns a boolean, checking whether the game is over or not 
  for row in board:
    for item in row:
      if item == 1:
        return False
  return True
def makemove(board, row, column):
  #Assume here that the item at row, column has not been fired at 
  #This move should change the board's state!
  #The only action we can take is firing at a board square
  if board[row][column] == 0:
    board[row][column] = 2
  elif board[row][column] == 1:
    board[row][column] = 3
  else:
    print("This square was already fired at!!!")

createboards()

while True:
  #We break out of this while loop when a game has ended    
  #We're going to ask the user to make a move
  print("Computer Board")
  specialprintboard(boardcomputer)
  print("Person Board")
  printboard(boardperson)

  #We make the person's move
  row = input("What row do you want to fire at?: ")
  col = input("What column do you want to fire at?: ")
  makemove(boardcomputer, int(row), int(col))


  #Now we want to make the computer's move    
  rowcol = random.choice(opensquaresleft)
  opensquaresleft.remove(rowcol)

  rowcomputer = rowcol[0]
  colcomputer = rowcol[1]

  makemove(boardperson, rowcomputer, colcomputer)

  #We need to change printboard and check whether someone won or not
  #Lastly, we want to randomly assign ship locations in createboard
  if (gameover(boardcomputer) and gameover(boardperson)):
    print("It's a tie!")
    break
  elif (gameover(boardcomputer)):
    print("You won!")
    break
  elif (gameover(boardperson)):
    print("You lost!")
    break
