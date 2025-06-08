"""
1. check if x is power of 2
2. check if k-th bit is set:  x & (1<<k)
3. toggle the k-th bit : x ^ (1<<k)
4. set the k-th bit: x | (1<<k)
5. unset the k-th bit: x & ~(1<<k)
6. find out x % 2^k  = x & ((1<<k) -1 )
7. swap x and y without more space:
    x = x ^ y
    y = x ^ y
    x = x ^ y
8. Toggle x between A and B:
    x = A ^ B ^ x 
9. 
    A + B = (A ^ B) + 2*(A & B)
    A + B = (A | B) + (A & B)
10. finding no of bit "1" in x: 0(1)


"""
if x & (x-1)  == 0:
    print('x is power of 2')

k=3
if x & (1<<k) != 0:
    print("k-th bit of x is 1")

x ^ (1<<k) != 0:
    print("k-th bit of x is 1")
    
