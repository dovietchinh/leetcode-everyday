from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_is_valid(board,i,j):
            print('check_is_valid',i,j, board[i][j])

            for a in range(9):
                if a == i:
                    continue 
                if  board[i][j] == board[a][j]:
                    return False 
            for a in range(9):
                if a == j:
                    continue 
                if board[i][j] == board[i][a]:
                    return False
            for a in range(3):
                for b in range(3):
                    if ((i//3*3+a) == i) and ((j//3*3+b) == j):
                        continue
                    if board[i][j] == board[i//3*3+a][j//3*3+b]:
                        return False
            return True
        def findSolution(board,i=0,j=0):
            print('findSolution',i,j)
            if i==9 and j==8:
                return True 
            if i==9:
                return findSolution(board,0,j+1)
            if board[i][j] != '.':
                return findSolution(board,i+1,j)
            else:
                for k in range(1,10):
                    print('k: /',k)
                    board[i][j] = str(k)
                    check = check_is_valid(board,i,j)
                    if check:
                        if findSolution(board,i+1,j):
                            return True 
                        else:
                            board[i][j] = '.'
                            continue
                    else:
                        board[i][j] = '.'
                        continue 
                return False
        a = findSolution(board)
        print('boeard: ',board)
        return a
                    
                
        # for i in range(9):
        #     for j in range(9):
        #         if board[i][j] != '.':
        #             if not self.is_valid(board, i, j):
        #                 return False
        

if __name__ == '__main__':
    board_true= [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    board_false = [["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    board_test = [[".","8","7","6","5","4","3","2","1"]
            ,["2",".",".",".",".",".",".",".","."]
            ,["3",".",".",".",".",".",".",".","."]
            ,["4",".",".",".",".",".",".",".","."]
            ,["5",".",".",".",".",".",".",".","."]
            ,["6",".",".",".",".",".",".",".","."]
            ,["7",".",".",".",".",".",".",".","."]
            ,["8",".",".",".",".",".",".",".","."]
            ,["9",".",".",".",".",".",".",".","."]]
    r = Solution().isValidSudoku(board)
    print(r)