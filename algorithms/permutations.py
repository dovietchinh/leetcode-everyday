
def make_permutations(n,tail=[]): 
    #this is backtracking
    res = []
    
    if not hasattr(make_permutations,'res'):
        make_permutations.res = []
    if len(n)==0:
        return [tail]
    for i in range(len(n)): 
        asd = make_permutations(n[:i]+n[i+1:],[*tail,n[i]])
        res += asd
    return res 

r = make_permutations([1,2,3,4])
print(r)
# print(make_permutations.res)