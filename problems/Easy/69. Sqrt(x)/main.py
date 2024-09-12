from typing import *
class Solution:
    def mySqrt(self, x: int) -> int:
        if x ==0 or x == 1:
            return x
        start = 1
        end = x 
        while start <= end: 
            mid = (start + end) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                start = mid + 1
            else:
                end = mid - 1 
        mid = (start + end) // 2
        return mid


if __name__ == '__main__':
    import random
    for _ in range(100):
        x = random.randint(1,1000)
        a = int(x**0.5)
        b = Solution().mySqrt(x)
        if a != b:
            print(a,b)
            