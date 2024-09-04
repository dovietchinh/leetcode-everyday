
# basic top-down approach ( recursive approach)
def fibonacci(index):
    if index == 0 : 
        return 0
    elif index == 1:
        return 1
    else:
        return fibonacci(index-1) + fibonacci(index-2)

top-down approach with memorization
def fibonacci_memoization(index):
    if not hasattr(fibonacci_memoization,'memo'):
        fibonacci_memoization.memo = {} 
    if index in fibonacci_memoization.memo:
        return fibonacci_memoization.memo[index]
    if index == 0 : 
        return 0
    elif index == 1:
        return 1
    else:
        memo_index = fibonacci_memoization(index-1) + fibonacci_memoization(index-2)
        fibonacci_memoization.memo[index] = memo_index
        return memo_index

def fibonacci_memoization(index,memo={}):
    if index in memo:
        return memo[index]
    if index == 0 : 
        return 0
    elif index == 1:
        return 1
    else:
        memo_index = fibonacci_memoization(index-1,memo) + fibonacci_memoization(index-2,memo)
        memo[index] = memo_index
        return memo_index




# bottom-up approach
def fibonacci_bottom_up(index):
    if index == 0 : 
        return 0
    elif index == 1:
        return 1
    else:
        memo = [0,1]
        for i in range(2,index+1):
            memo.append(memo[i-1] + memo[i-2])
        return memo[index]


import time 
t1 = time.time()
r = fibonacci(40)

t2 = time.time() - t1

t3 = time.time()
r = fibonacci_memoization(40)
print(r)
t4 = time.time() - t3
print(t2,t4)
print(t2/t4)

t5 = time.time()
r = fibonacci_bottom_up(40)
print(r)
t6 = time.time() - t5
print(t6)
print(t2/t6)