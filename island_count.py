"""Island Count
Given a 2D array binaryMatrix of 0s and 1s, implement a function getNumberOfIslands that returns the number of islands of 1s in binaryMatrix.

An island is defined as a group of adjacent values that are all 1s. A cell in binaryMatrix is considered adjacent to another cell if they are next to each either on the same row or column. Note that two values of 1 are not part of the same island if they’re sharing only a mutual “corner” (i.e. they are diagonally neighbors).

Explain and code the most efficient solution possible and analyze its time and space complexities.

Example:

input:  binaryMatrix = [ [0,    1,    0,    1,    0],
                         [0,    0,    1,    1,    1],
                         [1,    0,    0,    1,    0],
                         [0,    1,    1,    0,    0],
                         [1,    0,    1,    0,    1] ]

output: 6 # since this is the number of islands in binaryMatrix.
"""


##straign forward DFS solution O(n*m)  time and space complexity 

def get_number_of_islands(binaryMatrix):
  
  
  
  
  if not binaryMatrix:
    return 0 
  
  number_of_island = 0
  
  row = len(binaryMatrix)
  col = len(binaryMatrix[0])
  
  for i in range(row):
    for j in range(col):
      if binaryMatrix[i][j] ==1:
        dfs_iterative(binaryMatrix, i, j)
        number_of_island+=1 
  
  
  return  number_of_island


def dfs_iterative(grid, r, c):
  
  #print(grid)
  stack = []
  
  stack.append((r,c))
      
    
  directions = [(0, 1), (1,0), (0, -1), (-1, 0)]
  while stack:
    r, c = stack.pop() #0, 1
    grid[r][c] =0
    for dir_x, dir_y in directions:
      

      new_r = r + dir_x
      new_c = c+ dir_y
      
      if 0<=new_r<=len(grid)-1 and 0<=new_c<=len(grid[0])-1 and grid[new_r][new_c] ==1:
        stack.append((new_r, new_c))
        grid[new_r][new_c] =0 
      

    # go in all four directions
    

def dfs(grid, r, c):
  #print(grid)
  if r <0 or r >= len(grid) or c <0 or c >=len(grid[0])  or grid[r][c] !=1:
    return 
  
  grid[r][c] =0 
  dfs(grid, r+1, c)
  dfs(grid, r-1, c)
  dfs(grid, r, c+1)
  dfs(grid, r, c-1)
  
  
  
  
  