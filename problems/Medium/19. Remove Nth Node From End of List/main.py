from typing import *
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow_ptr = head 
        fast_ptr = head 
        for _ in range(n):
            fast_ptr = fast_ptr.next
        if fast_ptr is None:
            head = head.next
            return head
        while fast_ptr.next is not None:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next
        slow_ptr.next = slow_ptr.next.next
        return head 

if __name__ == '__main__':
    head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
    head = Solution().removeNthFromEnd(head,1)
    while head is not None:
        print(head.val)
        head = head.next
    
