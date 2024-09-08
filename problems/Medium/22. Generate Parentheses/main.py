
from typing import *
class Solution:
    def generateParenthesis(self, n: int):
        if n==1:
            return ["()"]
        else:
            results = set()
            for tree in self.generateParenthesis(n-1):
                all_indexs = self.find_all_index_in_list(tree,")")
                for index in all_indexs:
                    new_tree = tree
                    new_tree = new_tree[:index] + "()" + new_tree[index:]
                    results.add(new_tree)
                results.add(tree+"()")
            return results            
    def find_all_index_in_list(self,list_,value):
        results = []
        current_index = -1
        while(1):
            try:
                current_index = list_.index(value,current_index+1)
                results.append(current_index)
            except ValueError:
                break
        return results

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # stack + backtracking 
        results = []

        def backtracking(count=0,stack=""):
            nonlocal results
            # print('count-stack: ',count,stack)
            if len(stack) == 2*n:
                if count == 0:
                    results.append(stack)
                return
            if count > n:
                return
            if count < 0:
                return
            for i in ['(',')']:
                if i == '(':
                    backtracking(count+1,stack + i)
                else:
                    backtracking(count-1,stack + i)

        backtracking()
                
        return results

if __name__ == '__main__':
    # pass
    a = Solution().generateParenthesis(3)
    print(a)