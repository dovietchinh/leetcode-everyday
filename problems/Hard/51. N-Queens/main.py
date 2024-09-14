from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # res = [['.'*n for _ in range(n)]]
        def putQ(queens):
            # print('queens: ',queens)
            if len(queens) == n:
                res = ['.'*n for _ in range(n)]
                # print('res: ',res)
                for i in range(n):
                    
                    res[i] = res[i][:queens[i]] + 'Q' + res[i][queens[i]+1:]
                print(res)
                return
            invalid_sum = [z+queens[z] for z in range(len(queens))]
            invalid_diff = [z-queens[z] for z in range(len(queens))]
            # print('invalid_sum: ',invalid_sum)
            # print('invalid_diff: ',invalid_diff)
            for i in range(n):
                if i in queens:
                    continue
                # if any(abs(i-j) == len(queens)-k for k,j in enumerate(queens)):
                #     continue
                if len(queens) + i in invalid_sum:
                    continue 
                if len(queens) - i in invalid_diff:
                    continue
                putQ(queens+[i])
        putQ([])
                

if __name__ == '__main__':
    Solution().solveNQueens(8)
    # for i in r:
    #     print(i)