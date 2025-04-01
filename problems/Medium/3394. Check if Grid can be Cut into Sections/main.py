# https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections/description
from typing import *
class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
            
        # check x-cordinate
        # print('start check x')
        rect_sort_x = sorted(rectangles,key=lambda x: x[0])
        p_end = 0
        count_x = 0
        for start,_,end,_ in rect_sort_x:
            if start >= p_end and p_end !=0 :
                count_x += 1
                # print(f'cut between {p_end} {start} {end}')
            p_end = max(end,p_end)
        if count_x >= 2:
            # print('count_x: ',count_x)
            return True 

        # check y-cordinate
        # print('start check y')
        rect_sort_y = sorted(rectangles,key=lambda x: x[1])
        # print('rect_sort_y: ',rect_sort_y)
        p_end = 0
        count_y = 0
        for _,start,_,end in rect_sort_y:
            # print(f'p_end,start,end: {p_end} {start} {end}')
            if start >= p_end and p_end !=0 :
                count_y += 1
                # print(f'cut between {p_end} {start} {end}')
            p_end = max(end,p_end)
        if count_y >= 2:
            # print('count_y: ',count_y)
            return True 
        # print('count_x: ',count_x)
        # print('count_y: ',count_y)
        return False

            



            



if __name__ == '__main__':
    n = 5
    rectangles = [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]
    n = 4
    rectangles = [[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]]
    n = 4
    rectangles = [[0,2,2,4],[1,0,3,2],[2,2,3,4],[3,0,4,2],[3,2,4,4]] # False
    r = Solution().checkValidCuts(n,rectangles)
    print('r: ',r)
    