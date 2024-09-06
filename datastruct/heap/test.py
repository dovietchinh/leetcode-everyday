import heapq
l1 = [9,5,1,7,3,11]
l2 = [2,4,10,8,6,12]

heapq.heapify(l1)
heapq.heapify(l2)
print('l1: ',l1)
print('l2: ',l2)
def heapify(arr, N, i):
    print('i: ',i)
    smallest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < N and arr[smallest] > arr[l]:
        smallest = l

    # See if right child of root exists and is
    # greater than root
    if r < N and arr[smallest] > arr[r]:
        smallest = r

    # Change root, if needed
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, N, smallest)

# The main function to sort an array of given size
arr = [9,5,1,7,3,11]
heapify(arr, len(arr), 0)
print('arr: ',arr)