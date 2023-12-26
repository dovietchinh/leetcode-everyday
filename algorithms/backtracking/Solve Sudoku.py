# N-Queen Problem
# Solve Sudoku
# M-coloring problem
# Rat in a Maze
# The Knight’s tour problem
# Permutation of given String

def SolveSudoKu(S,x=0,y=0):
    # print(x,y,S[x][y])
    if x == 9:
        if y==8:
            print(S)
            print('return')
            return 
        x = 0
        y += 1
    if S[x][y] != 0:
        SolveSudoKu(S,x+1,y)
    else:
        for k in range(1,10):
            if isSafe(S,x,y,k):
                S[x][y] = k
                SolveSudoKu(S,x+1,y)
                S[x][y] = 0
    
            
            

def isSafe(grid, row, col, num):
   
    # Check if we find the same num
    # in the similar row , we
    # return false
    for x in range(9):
        if grid[row][x] == num:
            return False
 
    # Check if we find the same num in
    # the similar column , we
    # return false
    for x in range(9):
        if grid[x][col] == num:
            return False
 
    # Check if we find the same num in
    # the particular 3*3 matrix,
    # we return false
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True
 




if __name__ == '__main__':
    grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]
    SolveSudoKu(grid,0,0)