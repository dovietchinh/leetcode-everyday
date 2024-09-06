import heapq
import random
def heapify(arr,N,i):
    # size = len(arr)
    largest = i  # Initialize largest as root
    left = 2 * i + 1     # left = 2*i + 1
    right = 2 * i + 2     # right = 2*i + 2
    if largest < N/2-1 and arr[largest] < arr[left]:
        largest = left
    if largest < N/2-1 and arr[largest] < arr[right]:   
        largest = right 
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr,N,largest)
    # return arr

arr = random.sample(range(1,100),10)
print('arr before heapify: ',arr)
heapify(arr,len(arr),0)
print('arr after heapify: ',arr)
