from typing import *
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        queue = []
        for i in range(m):
            if board[i][0] == 'O':
                queue.append((i,0))
            if board[i][n-1] == 'O':
                queue.append((i,n-1))
        for j in range(n):
            if board[0][j] == 'O':
                queue.append((0,j))
            if board[m-1][j] == 'O':
                queue.append((m-1,j))
        visited = set()
        while queue:
            i,j = queue.pop(0)
            if (i,j) in visited:
                continue
            visited.add((i,j))
            if j<n-1 and board[i][j+1] == 'O':
                queue.append((i,j+1))
            if j!=0 and board[i][j-1] == 'O':
                queue.append((i,j-1))
            if i<m-1 and board[i+1][j] == 'O':
                queue.append((i+1,j))
            if i!=0 and board[i-1][j] == 'O':
                queue.append((i-1,j))
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i,j) not in visited:
                    board[i][j] = 'X'
        






if __name__ == '__main__':
    board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    board = [["X"]]
    Solution().solve(board)
    # print('result->', board)
    for i in board:
        print(i)