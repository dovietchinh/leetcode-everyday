results = []

def backtracking(nums,tail=[]):
    if len(nums) == 0:
        results.append(tail)
        return
    for i in range(len(nums)):
        backtracking(nums[:i] + nums[i+1:],tail + [nums[i]])

backtracking([1,2,3])
print(results)
