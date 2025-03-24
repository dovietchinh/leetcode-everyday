from typing import *
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def print(self):
        print(self.val,end='->')
        if self.next:
            self.next.print()
        else:
            print()

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head 
        slow = head
        fast = head 
        pre_slow = None
        pre_fast = None 
        if k == 1:
            p = head.next 
            pre_p = head 
            # print('head.next.val: ',head.next.val)
            while p.next:
                p = p.next 
                pre_p = pre_p.next
            pre_p.next = head 
            p.next = head.next 
            # print('head.next.val: ',p.next.val)
            # print('p.next.val: ',p.next.val)
            head.next = None 
            return p
        if head.next.next is None:
            p = head.next
            p.next = head 
            head.next = None 
            return p
            

        for i in range(k-1):
            fast = fast.next 
            pre_fast = pre_fast.next if pre_fast else head 
        pre_p = pre_fast 
        p = fast   # point to k-th
        
        print('slow.val: ',slow.val)
        print('p.val: ',p.val)
        print('fast.val: ',fast.val)

        while fast.next:
            pre_fast = pre_fast.next if pre_fast else head 
            fast = fast.next 
            pre_slow = pre_slow.next if pre_slow else head
            slow = slow.next 
        
        # fast point to final 

        print('slow.val: ',slow.val)
        print('p.val: ',p.val)
        print('fast.val: ',fast.val)

        # swap slow and p
        if slow is head:
            next_slow = slow.next 
            slow.next = None 
            p.next = next_slow 
            pre_p.next = slow 
            return p
        if p is head:
            next_slow = slow.next 
            slow.next = None 
            p.next = next_slow 
            pre_p.next = slow 
            return p
            
        if slow is p:
            return head
        if slow.next is p:
            slow.next = p.next 
            p.next = slow 
            pre_slow.next = p 
            return head 
        if p.next is slow:
            p.next = slow.next 
            slow.next = p
            pre_p.next = slow 
            return head 
        if slow is not head:
            next_slow = slow.next 
            next_p = p.next 

            pre_slow.next = p 
            p.next = next_slow 

            pre_p.next = slow 
            slow.next = next_p 
            return head 
        





if __name__ == '__main__':
    head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,ListNode(6,ListNode(7,ListNode(8,ListNode(9,ListNode(10))))))))))
    head = ListNode(100,ListNode(90))
    # [7,9,6,6,7,8,3,0,9,5]
    k = 2
    head.print()
    r = Solution().swapNodes(head,k)
    r.print()