class Solution:
    def integerReplacement(self, n: int) -> int:
        count = 0
        while n!=1:
            if n%2==0:
                n = n//2
            elif n == 3:
                n -= 1
            elif n%4 == 1:
                n -= 1
            elif n%4 == 3:
                n += 1
            count += 1
        return count

if __name__ == '__main__':
    r = Solution().integerReplacement(65535)
    print(r)