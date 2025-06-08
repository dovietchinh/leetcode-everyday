# Python Program for Maximum Subarray Sum using Kadane's Algorithm

# Function to find the maximum subarray sum
def maxSubarraySum(arr):
    
    res = arr[0]
    maxEnding = arr[0]

    for i in range(1, len(arr)):
        maxEnding = max(maxEnding + arr[i], arr[i])
        res = max(res, maxEnding)
    return res

arr = [2, 3, -8, 7, -1, 2, 3]
print(maxSubarraySum(arr))