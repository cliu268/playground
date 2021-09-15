# This is Ryan's final project: Maze puzzle code
# for context and more details watch class recording for week9 and week10
import random
def createMaze(m, n, numRooms):
  totalmaze = []
  for i in range(m):
    temp = []
    for j in range(n):
      temp.append(0)
    totalmaze.append(temp)
  
  created = 0
  xlist = []
  ylist = []
  while created < numRooms:
    row = random.randint(0, m-1)
    col = random.randint(0, n-1)
    if totalmaze[row][col] == 0:
      totalmaze[row][col] = 1
      xlist.append(row)
      ylist.append(col)
      created +=1
  

  for i in range(len(xlist)-1):
    startx = xlist[i]
    starty = ylist[i]

    endx = xlist[i+1]
    endy = ylist[i+1]

    while startx != endx:
      totalmaze[startx][starty] = 1
      if (startx < endx):
        startx +=1
      else:
        startx -= 1
    while starty != endy:
      totalmaze[startx][starty] = 1
      if (starty < endy):
        starty +=1
      else:
        starty -= 1

  totalmaze[xlist[0]][ylist[0]] =  2 #This is my start
  totalmaze[xlist[-1]][ylist[-1]] =  3 #This is my end
  return totalmaze

def displayMaze(maze):
  # 0 is a wall
  # 1 is a path
  for i in maze:
    savestring = ""
    for j in i:
      if j == 0:
        savestring = savestring + '_ '
      elif j == 1:
        savestring = savestring + 'O '
      elif j == 2 or j == 5:
        savestring = savestring + 'S '
      elif j == 3:
        savestring = savestring + 'E '
      elif j == 4:
        savestring = savestring + 'H '
    print(savestring)


# displayMaze(createMaze(20, 20, 15))
def dfs(maze, i, j):
  if i < 0  or j < 0 or i >= len(maze) or j >= len(maze[0]):
    return False
  elif maze[i][j] == 0 or maze[i][j] == 4 or maze[i][j] == 5:
    return False
  elif maze[i][j] == 3:
    displayMaze(maze)
    return True
  else:
    if maze[i][j] != 2:
      maze[i][j] = 4
    else:
      maze[i][j] = 5
    directions = [[0,1], [1,0], [0, -1],  [-1, 0]]
    checker = False
    for ichange, jchange in directions:
      if dfs(maze, i + ichange, j+jchange):
        checker = True
        break
    if not checker:
      if maze[i][j] == 4:
        maze[i][j] = 1
      else:
        maze[i][j] = 2
      return False
    return True

def bfs(maze, level, frontier):
  for i, j in frontier:
    if maze[i][j] == 3:
      displayMaze(maze)
      return level
    if maze[i][j] != 2:
      maze[i][j] = 4
  returnlistfrontier = []
  for i, j in frontier:
    directions = [[0,1], [1,0], [0, -1],  [-1, 0]]
    for ichange, jchange in directions:
      newi = i + ichange
      newj = j + jchange
      if newi < 0 or newj < 0 or newi >= len(maze) or newj >= len(maze[0]) or maze[newi][newj] == 0 or maze[newi][newj] == 2 or maze[newi][newj] == 4:
        continue
      else:
        returnlistfrontier.append([newi, newj])
  return bfs(maze, level + 1, returnlistfrontier)

maze = createMaze(20, 20, 15)
x = 0
y = 0
for i in range(len(maze)):
  for j in range(len(maze[0])):
    if maze[i][j] == 2:
      x = i
      y = j
      break
print(bfs(maze, 0, [[x, y]]))

# Work with the maze generation to create impossible mazes
# Using some sot of GUI library like TKinter to render the maze not using console output
