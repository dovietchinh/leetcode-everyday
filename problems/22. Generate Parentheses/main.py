
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


            





            

        



if __name__ == '__main__':
    # pass
    a = Solution().generateParenthesis(2)
    print(a)