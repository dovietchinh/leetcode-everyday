import bisect

def binary_search(arr, target):
    size = len(arr)
    if len(arr) == 0:
        return -1
    if len(arr) == 1:
        return 0 if arr[0] == target else -1
    left = 0 
    right = size - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    

print(binary_search([0,1,2,3,4,5,6,7,8,9,10], 5)) # 4