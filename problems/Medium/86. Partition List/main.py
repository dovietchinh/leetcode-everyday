from typing import *
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def print(self):
        print(self.val, end='->')
        if self.next:
            self.next.print()
        else:
            print()
def create_list_node(nums):
    if len(nums) == 0:
        return None
    head = ListNode(nums[0])
    p = head
    for i in range(1,len(nums)):
        p.next = ListNode(nums[i])
        p = p.next
    return head



class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # hande edge case
        if head is None:
            return head
        if head.next is None:
            return head
        l1 = None
        l2 = None
        pointer1 = None
        pointer2 = None
        p = head
        while p:
            if p.val < x:
                if l1 is None:
                    l1 = p 
                    pointer1 = p
                else:
                    l1.next = p 
                    l1 = p
            else: # p.val >= x 
                if l2 is None:
                    pointer2 = p
                    l2 = p 
                else:
                    l2.next = p 
                    l2 = p 
            p = p.next
        if l1:
            l1.next = pointer2
        if l2:
            l2.next = None
        if pointer1:
            return pointer1
        else:
            return pointer2
                    

            
        


if __name__ == '__main__':
    head = create_list_node([1,2,1])
    head.print()
    r = Solution().partition(head,-1 )
    r.print()


    # print(r)