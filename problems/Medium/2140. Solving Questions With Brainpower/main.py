from typing import *
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        size = len(questions)
        # cache = [None for _ in range(size)]
        cache = {}
        def dp(i):  
            print('i: ',i)
            nonlocal cache 
            if i in cache:
                return cache[i]
            
            if i<0:
                return 0 
            if i==0:
                return questions[-1][0]
            points, brainpower = questions[size-1-i]
            cache[i] = max(points+dp(i-1-brainpower),dp(i-1))
            return cache[i]
        r = dp(size-1)
        # print('cache: ',cache)
        return r


if __name__ == '__main__':
    questions = [[72,5],[36,5],[95,5],[50,1],[62,1],[14,3],[72,5],[86,2],[43,3],[51,3],[14,1],[91,5],[47,4],[72,4],[63,5],[40,3],[68,1],[8,3],[84,5],[7,5],[40,1],[35,3],[66,2],[39,5],[40,1],[92,3],[67,5],[34,3],[84,4],[75,5],[6,1],[71,3],[77,3],[25,3],[53,3],[32,3],[88,5],[18,2],[21,3],[78,2],[69,5],[45,4],[94,2],[70,1],[85,2],[7,2],[68,4],[71,4],[57,2],[12,5],[53,5],[51,3],[46,1],[28,3]]
    r = Solution().mostPoints(questions)
    print('r: ',r)