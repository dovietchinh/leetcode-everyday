# Quick Sort
# Time Complexity: O(nlogn)
# Space Complexity: O(logn)
# Worst Case: O(n^2) when the array is already sorted => no stable
def partition(arr, low, high):
  
    # Choose the pivot
    pivot = arr[high]
    
    i = low - 1
    
    # Traverse arr[low..high] and move all smaller
    # elements on the left side. Elements from low to 
    # i are smaller after every iteration
    for j in range(low, high):
        
        print(i,j,arr)
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            print('swap')
    
    # Move pivot after smaller elements and
    # return its position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# The QuickSort function implementation
def quick_sort(arr, low, high):
    if low < high:
        # pi is the partition return index of pivot
        pi = partition(arr, low, high)
        print('pi',pi)
        # Recursion calls for smaller elements
        # and greater or equals elements
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

if __name__ == "__main__":
    arr = [6,5,4,3,2,1][::-1]

    quick_sort(arr, 0, len(arr) - 1)