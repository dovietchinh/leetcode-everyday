import collections
class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = collections.Counter(s)
        size = 0 
        keys = list(counter.keys())
        print('counter: ',counter)        
        for k in keys:
            v = counter[k]
            i = v//2 * 2
            size += i
            if counter[k] == i:
                counter.pop(k)
        print('counter:', counter)
        if counter:
            size += 1
        return size

if __name__ == '__main__':
    s = "abccccdd"
    s = "aaaa"
    r = Solution().longestPalindrome(s)
    print(r)

        