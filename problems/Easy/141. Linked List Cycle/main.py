from typing import *
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def create_list_node_cycle(nums,pos):
    if len(nums) == 0:
        return Node 
    l = []
    for i in nums:
        l.append(ListNode(i))
    for i in range(len(nums)-1):
        l[i].next = l[i+1]
    if pos >= 0:
        l[-1].next = l[pos]
    return l[0]
    


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # handle edge case 
        if head is None or head.next is None:
            return False
        if head.next is head:
            return True 

        p1 = head 
        p2 = head 
        count_meet = 0
        while p2 or p2.next:
            if p1 is p2:
                count_meet += 1
                if count_meet != 1:
                    return True 
            p1 = p1.next
            p2 = p2.next.next if p2.next else None 
        return False 

if __name__ == '__main__':
    head = create_list_node_cycle([3,2,0,-4],1)


        