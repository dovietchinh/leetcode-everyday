from typing import *
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        size_1 = len(version1)
        size_2 = len(version2)
        a = version1.split('.')
        b = version2.split('.')
        len_a = len(a)
        len_b = len(b)
        for i in range(min(len_a,len_b)):
            print('i: ',i)
            i_1 = a[i]
            i_1 = int(i_1) if len(i_1)!=0 else 0
            i_2 = b[i]
            i_2 = int(i_2) if len(i_2)!=0 else 0
            if i_1 < i_2:
                print('return here 1')
                return -1
            elif i_1 > i_2:
                return 1
            elif i_1 == i_2:
                continue
            else:
                print('error')
        if len_a < len_b:
            print('1')
            for i in range(len_b - len_a):
                if int(b[i+len_a]) !=0:
                    return -1
            return 0
        elif len_a > len_b:
            print('2')
            for i in range(len_a - len_b):
                if int(a[i+len_b]) != 0:
                    return 1 
            return 0
        else:
            print('3')
            return 0

if __name__ == '__main__':
    version1 = "1.0.1"
    version2 = "1"
    r = Solution().compareVersion(version1,version2)
    print('r: ',r)


        


        



