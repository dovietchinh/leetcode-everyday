from typing import *
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies = set(supplies)
        data = {}
        for i in range(len(recipes)):
            data[recipes[i]] = ingredients[i]
        # print('data: ',data)
        # exit()
        cache = {}
        # print('data: ',data['x'])
        count = 0
        def dfs(node):
            # dfs 
            nonlocal cache
            nonlocal count 
            # count += 1
            # if count == 30:
            #     exit()
            print('node: ',node, cache)
            if node in cache:
                return cache[node]
            if node in supplies:
                cache[node] = 1
                return True
            if node not in data:
                cache[node] = 1 if node in supplies else 0 
                return cache[node]
            cache[node] = 0
            for i in data[node]:
                if dfs(i) == 0:
                    cache[i] = 0
                    return 0
            cache[node] = 1
            return 1
        # a = dfs('e')
        # print('a: ',a)

        results = []
        for i in  recipes:
            if dfs(i) == 1:
                results.append(i)
        return results

if __name__ == '__main__':
    r = ["ju","fzjnm","x","e","zpmcz","h","q"]
    i = [["d"],["hveml","f","cpivl"],["cpivl","zpmcz","h","e","fzjnm","ju"],["cpivl","hveml","zpmcz","ju","h"],["h","fzjnm","e","q","x"],["d","hveml","cpivl","q","zpmcz","ju","e","x"],["f","hveml","cpivl"]]
    s = ["f","hveml","cpivl","d"]
    # r = ["bread"]
    # i = [["yeast","flour"]]
    # s = ["yeast","flour","corn"]
    r = Solution().findAllRecipes(r,i,s)
    print('r: :',r)