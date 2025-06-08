import heapq 

a = [9,1,8,9]
q = []
for i in range(len(a)-1,-1,-1):
    heapq.heappush(q,(-a[i],-i))

print(q)
