import heapq
 
# initializing list
li = [5, 7, 9, 1, 3]
 
# using heapify to convert list into heap
heapq.heapify(li)
print(type(li))
print(li)

heapq.heappush(li, 4)
heapq.heappush(li, 20)
print(li)
# print('heapq: ',heapq)
# printing created heap
# print ("The created heap is : ",(list(li)))
# while True:
    # print(heapq.heappop(li))


l1 = [9,5,1,7,3,11]
l2 = [2,4,10,8,6,12]

heapq.heapify(l1)
heapq.heapify(l2)
print('l1: ',l1)
print('l2: ',l2)
