from typing import List
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        n = len(beginWord)



        
def check_differ(a,b):
    count = 0
    for i,j in zip(a,b):
        if i!=j:
            count += 1
    return count==1




if __name__ == '__main__':
    pass