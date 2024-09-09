from typing import *
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        size = len(strs)
        def find_prefix(arr,left,right):        
            print('arr: ',arr, 'left: ',left, 'right: ',right)  
            if left <= right:
                if right - left > 1:
                    mid = (left + right) // 2
                    print('mid: ', mid)
                    pre_1 = find_prefix(arr,left,mid)
                    pre_2 = find_prefix(arr,mid+1,right)
                    print('pre_1, pre_2: ',pre_1, pre_2)
                    if pre_1 is None and pre_2: 
                        return pre_2
                    if pre_2 is None and pre_1:
                        return pre_1
                    if pre_1 is None and pre_2 is None:
                        return None
                    l1 = len(pre_1)
                    l2 = len(pre_2)
                    if l1 == 0 or l2 == 0:
                        print('return empty')
                        return ""
                    for index in range(min(l1,l2)):
                        if pre_1[index] != pre_2[index]:
                            return pre_1[:index]
                    return pre_1[:index+1]
                elif (right - left) == 0: 
                    print('return 0')
                    return arr[left]
                elif (right - left) == 1:
                    l1 = len(arr[left])
                    l2 = len(arr[right])
                    if l1 == 0 or l2 == 0:
                        return ""
                    for index in range(min(l1,l2)):
                        if arr[left][index] != arr[right][index]:
                            return arr[left][:index]
                    return arr[left][:index+1]
            return None
                    
        return find_prefix(strs,0,size-1)

        


        


        

if __name__ == '__main__':
    
    strs = ["ab","a"]
    r = Solution().longestCommonPrefix(strs)
    print('r: ',r)
    
    
        