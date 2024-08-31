"""
Floyd's Cycle-Finding (Runner pointer):
    algorithms using two pointer , moving through sequence with different speeds.
    This technique is use to find a loop in a linked list.
    Fast-pointer moving twice as fast as the slow-pointer.
"""

class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None 

class LinkList:
    def __init__(self):
        self.head = None 
    
    def append(self,node):
        if self.head is None:
            self.head = node
        ptr = self.head
        while ptr.next is not None:
            ptr = ptr.next 
        ptr.next = node 
    
    def insert(self,node,index):
        if index ==0 :
            self.head = 
        ptr = self.head
        for _ in range(index-1):
            ptr = ptr.next
            if ptr is None:
                print("Out of bounds")
                return 
        node.next = ptr.next 
        ptr.next = node 

            
    

            
            