from typing import List

def solve(board,x=0,y=0):
    # print('x,y: ',x,y)
    if x==9:
        if y==8:
            # print('board: ',board)
            # # exit()
            return True
        x = 0
        y += 1

    if board[x][y] !='.':
        if solve(board,x+1,y):
            return True

    else:
        for value in range(1,10):
            value = str(value)
            if not check_board(board,x,y,value):
                continue
            board[x][y] = value
            if solve(board,x+1,y):
                return True
            board[x][y] = '.'

def check_board(board,x,y,value):
    for i in range(9):
        if board[x][i] == value:
            return False 
        if board[i][y] == value:
            return False 
    a = x//3 
    b = y//3
    for i in range(a*3, a*3+3):
        for j in range(b*3,b*3+3):
            if board[i][j] == value:
                return False
    return True

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        solve(board)
if __name__ == '__main__':
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    Solution().solveSudoku(board)
    print('board: ',board)