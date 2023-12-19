class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        before = self.countAndSay(n-1)
        old_value = None
        count = 0
        result = ""
        for i in before:
            if old_value is None:
                count = 1
                old_value = i
                continue
            if old_value == i:
                count += 1
            else:
                result += str(count) + old_value
                count = 1
            old_value = i
        result += str(count) + old_value
        return result
            
if __name__ == '__main__':
    r = Solution().countAndSay(4)
    print(r)
            

            