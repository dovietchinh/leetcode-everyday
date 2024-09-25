from typing import *
class Solution:
    def isNumber(self, s: str) -> bool:
        size = len(s)
        start = 0 
        end = 0
        number = ['0','1','2','3','4','5','6','7','8','9']
        s = s.replace('E','e')
        s = s.replace('+','s')
        s = s.replace('-','s')
        for i in number:
            s = s.replace(i,'n')
        prev = None
        remove = []
        temp = ""
        for i in range(size):
            if prev and s[i] == prev:
                if prev!='n':
                    print('False')
                    return False
                else:
                    continue    
            prev = s[i]
            temp += s[i]
        pattern = [
            'sn.nesn.n',
            'n.nesn.n',
            'sn.nen.n',
            'n.nen.n',
        ]
        for j in range(5):
            p = ''
            p 
        return temp

    def combination(choices,index=0,tail=[]):
        if not hasattr(combination,'result'):
            combination.result = []
        choice = choices[index]
        for j in choice:
            combination(choices,index+1,[*tail,j])


         


if __name__ == '__main__':
    test_case = ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]
    for i in test_case:
        print(i,' : ',Solution().isNumber(i))