from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_is_valid(board,i,j,k):
            for a in range(9):
                if  board[i][j] == board[a][j]:
                    return False 
            for a in range(9):
                if board[i][j] == board[i][a]:
                    return False
            for a in range(3):
                for b in range(3):
                    if board[i][j] == board[i//3*3+a][j//3*3+b]:
                        return False
            return True
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                for k in range(9):
                    board[i][j] = str(k)
                        if not check_is_valid(board,i,j,str(k)):
                            break 
                        else: 
                            return True
                        
                    
        

                
        # for i in range(9):
        #     for j in range(9):
        #         if board[i][j] != '.':
        #             if not self.is_valid(board, i, j):
        #                 return False
        

if __name__ == '__main__':
    board = [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    r = Solution().isValidSudoku(board)
    print(r)