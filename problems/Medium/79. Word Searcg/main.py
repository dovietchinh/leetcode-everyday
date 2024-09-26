from typing import *
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        points = []
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    points.append((i,j))
        size = len(word)
        def dfs(node,level,visited):
            print(visited)
            if node in visited:
                return False
            if level == size - 1:
                return True 
            i,j = node
            if i!=0:
                if board[i-1][j] == word[level+1]:
                    if dfs((i-1,j),level+1,{*visited,(i,j)}):
                        return True
            if i!=m-1:
                if board[i+1][j] == word[level+1]:
                    if dfs((i+1,j),level+1,{*visited,(i,j)}):
                        return True
            if j!=0:
                if board[i][j-1] == word[level+1]:
                    if dfs((i,j-1),level+1,{*visited,(i,j)}):
                        return True
            if j!=n-1:
                if board[i][j+1] == word[level+1]:
                    if dfs((i,j+1),level+1,{*visited,(i,j)}):
                        return True
            
            return False
            
        for point in points:
            visited = set()
            if dfs(point,0,visited):
                return True
        return False
            


if __name__ == '__main__':
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    for i in board:
        print(i)
    word = "ABCB"
    print(word)
    r = Solution().exist(board, word)
    print(r)
    