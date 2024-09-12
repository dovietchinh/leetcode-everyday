from typing import *


class Heap:

    """
    Heap properties:
        1. Complete binary tree
        2. Max heap: parent >= children
        3. Min heap: parent <= children
        4. Heapify: O(logn)
        5. Build heap: O(n)
        6. Insert: O(logn)
        7. Delete: O(logn)
        8. Left node: 2i+1
        9. Right node: 2i+2
        10. Parent node: (i-1)//2
    """

    def __init__(self,arr,increase=True):

        self.arr = arr
        self.heapify(self.arr)
        self.increase = increase #max heap or min heap
    
    def heapify(self,arr):
        
        size = len(arr)
        for i in range(size//2-1,-1,-1):
            largest = i 
            left = 2*i+1
            right = 2*i+2
            if right < size and arr[largest] < arr[right]:
                largest = right
            if left < size and arr[largest] < arr[left]:
                largest = left
            
            if largest != i:
                arr[largest],arr[i] = arr[i],arr[largest]
                self.heapify(arr)
        

            
a = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]
h = Heap(a)
print(a)

import heapq
a = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]
heapq.heapify(a)
print(a)



            

            