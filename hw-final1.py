
# Saturday Classes Code! Ryan's Python beginner class final project: battleship game
import random

personboard = {}
computerboard = {}
computerpossiblemoves = []
def shipplacement(board, length, orientation):
  #If orientation is True ==> our ship is horizontal
  #If orientation is False ==> our ship is vertical
  if (orientation):
    #We go inside a horizontal case     
    #We need to generate the coordinates of our captain 
    captainrow = random.randrange(0, 8)
    captaincolumn = random.randrange(0, 9-length)
    for i in range(length):
      s = str(captainrow) + str(captaincolumn + i)
      board[s] = 1
  else:
    captainrow = random.randrange(0, 9-length)
    captaincolumn = random.randrange(0, 8)
    for i in range(length):
      s = str(captainrow + i) + str(captaincolumn)
      board[s] = 1
def createboards():
  global personboard
  global computerboard
  for row in range(8):
    for col in range(8):
      s = str(row) + str(col)
      personboard[s] = 0
      computerboard[s] = 0
      computerpossiblemoves.append(s)
  shipplacement(personboard, 4, False)
  shipplacement(computerboard, 4, False)

def displayboard(board):
  superstring = ''
  for row in range(8):
    for col in range(8):
      s = str(row) + str(col)
      superstring = superstring + str(board[s]) + ' '
    superstring = superstring + '\n'
  print(superstring)

def hiddendisplayboard(board):
  superstring = ''
  for row in range(8):
    for col in range(8):
      s = str(row) + str(col)
      if (board[s] == 0 or board[s] == 1):
        h = '_'
      elif (board[s] == 2):
        h = 'O'
      else:
        h = 'X'
      superstring = superstring + str(h) + ' '
    superstring = superstring + '\n'
  print(superstring)

def checkgamestate(board):
  for row in range(8):
    for col in range(8):
      s = str(row) + str(col)
      if (board[s] == 1):
        return False
  return True

def makemove(board, row, column):
  #This move should change the board's state!
  #The only action that we can take is firing at a square.
  s = str(row) + str(column)
  if (board[s] == 0):
    board[s] = 2
  elif (board[s] == 1):
    board[s] = 3
  else:
    #This should only happen when the user inputs a wrong input
    print("You already fired at that square!")
  
createboards()

while True:
  print("Computer Board")
  hiddendisplayboard(computerboard)
  print("Person Board")
  displayboard(personboard)

  userrow = input("What row do you want to fire at?")
  usercol = input("What column do you want to fire at?")
  usersquare = str(userrow) + str(usercol)

  makemove(computerboard, userrow, usercol)
  #We finished making our user's move, now onto the computers!

  computersquare = random.choice(computerpossiblemoves)
  makemove(personboard, int(computersquare[0]), int(computersquare[1]))
  computerpossiblemoves.remove(computersquare)

  if (checkgamestate(computerboard) and checkgamestate(personboard)):
    print("It's a tie!!!")
    break
  elif (checkgamestate(computerboard)):
    print("You won the game!")
    break
  elif (checkgamestate(personboard)):
    print("You lost the game!")
    break
