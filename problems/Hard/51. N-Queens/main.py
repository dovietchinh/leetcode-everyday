from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        results = set()
        count = 0
        check_valid_count = 0
        def putQueen(queens,tail=[],visit_row,visit_colums):
            nonlocal count
            count += 1
            if queens==0:
                temp = tuple(sorted(tail, key=lambda k:k[0]))
                results.add(temp)
                
            else:                
                for x in range(n):
                    for y in range(n):
                        if check_valid(x,y,tail):
                            putQueen(queens-1,[*tail,(x,y)])
        def check_valid(x,y,tail):
            nonlocal check_valid_count
            check_valid_count += 1
            for x_i,y_i in tail:
                if x==x_i or y==y_i:
                    return False
                if (x_i + y_i) == (x+y):
                    return False 
                if (x_i - y_i) == (x-y):
                    return False
            return True
        putQueen(n)
        print('count: ',count)
        print('check_valid_count: ',check_valid_count)
        output = []
        for r in results:
            S = ['.'*n]*n
            for x,y in r:
                S[x] = S[x][:y] + 'Q' + S[x][y+1:]
            output.append(S)
        return output
            
        # return results

if __name__ == '__main__':
    r = Solution().solveNQueens(5)
    for i in r:
        print(i)