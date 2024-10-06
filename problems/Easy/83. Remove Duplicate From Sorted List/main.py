from typing import *    
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = head 
        fast = head
        slow = head
        if not head or not head.next:
            return head
        while fast:
            if fast.val != slow.val: 
                slow.next = fast 
                slow  = fast
            
            
            fast = fast.next 
        slow.next = None
        return head
        

if __name__ == '__main__':
    head = None
    head = Solution().deleteDuplicates(head)
    while head:
        print(head.val)
        head = head.next
    
        