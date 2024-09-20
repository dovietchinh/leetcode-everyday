from typing import *
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_strs = []
        for i in strs:
            new_strs.append(''.join(sorted(i)))
        results = defaultdict(list)
        for index in range(len(new_strs)):
            key = new_strs[index]
            value = strs[index]
            results[key].append(value)
        return list(results.values())




if __name__ == '__main__':
    r = Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"])
    print(r)