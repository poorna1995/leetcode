def countPath(grid,row=0,col=0):
    memo ={}
    # pos= row + "," + col # position 
    pos = f"{row},{col}"
    
    print(pos)
# always think about out of bound # what should return
# whereshou kd i dont want to go
    # x or wall or snake
    if row>= len(grid) or col>=len(grid[0]) or grid[row][col] =='X':
        return 0
    # before going ask if it is in memo

    # check if you have arrived at given location

    if (row == len(grid)-1 and col == len(grid[0])-1):
        return 1
    # if you didn't reached 
    # ? retur the cache
    if pos in memo:
        return memo[pos]

    # memo[pos] = countPath( grid, row+1,col)+ countPath(grid, row,col+1)
    # return memo[pos]

    rightPath = countPath(grid,row,col+1)
    downPath = countPath(grid,row+1,col)
    memo[pos]= rightPath+downPath
    return memo[pos]



grid = [
    [' ', ' ', 'X', ' '],
    [' ', ' ', ' ', ' '],
    [' ', 'X', ' ', 'X'],
    [' ', ' ', ' ', ' ']
]
print(countPath(grid,row=0,col=0))