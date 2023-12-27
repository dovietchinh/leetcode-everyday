import itertools


print(list(itertools.permutations([1, 2, 3,4])))
# [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]


print(list(itertools.combinations('123', 2)))
# [('1', '2'), ('1', '3'), ('2', '3')]
print('product')
print(list(itertools.product([1,2,3], [4,5,6])))

# [(1, 4), (1, 5), (1, 6),
# (2, 4), (2, 5), (2, 6),
# (3, 4), (3, 5), (3, 6)]
print(list(itertools.product([1,2], repeat=3)))

# [(1, 1, 1), (1, 1, 2), (1, 2, 1), (1, 2, 2),
# (2, 1, 1), (2, 1, 2), (2, 2, 1), (2, 2, 2)]

def permutations(head, tail=[]):
    # test = []
    print('head,tail: ',head,tail)
    if not hasattr(permutations,'results'):
        permutations.results = []
    # print('head: ',head)
    if len(head) == 0:
        # print(tail)
        permutations.results.append(tail)
    else:
        for i in range(len(head)):
            permutations(head[:i] + head[i+1:], [*tail,head[i]])


print(permutations([1,2,3,4]))
print(permutations.results)
