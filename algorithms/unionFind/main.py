n = 10 
p = list(range(n))
rank = [1 for _ in range(n)]
def find(x):
    if p[x] == x:
        return x
    p[x] = find(p[x])
    return p[x]

def union(x,y):
    rootX,rootY = find(x),find(y)
    if rootX == rootY:  # x and y are already connected
        return False 
    
    if rank[x] <= rank[y]:
        p[x] = y 
        rank[x] += rank[y]
    else:
        p[y] = x 
        rank[y] += rank[x]
        
    return True 



