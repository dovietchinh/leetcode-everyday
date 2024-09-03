from typing import *            
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        TEXT = [None,None,"abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"] 
        res = []
        def make_combinations(d,tail=""):
            nonlocal res
            size = len(d)
            if len(d) == 0:
                if len(tail) != 0:
                    res.append(tail)
                return 
            else:
                # posible = TEXT[int(d[0])]
                posible = range(10)
                for p in posible:
                    make_combinations(d[1:],tail+str(p))
        make_combinations(digits)
        return res
            


            
    
if __name__ == '__main__':
    r = Solution().letterCombinations([1,1,1])
    print(r)