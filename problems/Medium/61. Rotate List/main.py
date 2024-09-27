from typing import *
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        slow = None
        fast = head
        count = None
        if not head:
            return head
        for i in range(k-1):
            if fast.next:
                fast = fast.next
            else:
                count = i +1 
                fast = head
                break
        if count:
            # print('count:', count)
            k = k % count
            # print('k:', k)
            for i in range(k-1):
                fast = fast.next
            # print('fast:', fast.val)
        if k == 0:
            return head

        while fast.next:
            if slow:
                slow = slow.next
            else:
                slow = head
            fast = fast.next
        if not slow:
            return head
        fast.next = head 
        head = slow.next
        slow.next =  None
        return head
        
        



if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    r = Solution().rotateRight(head,101)
    while r:
        print(r.val)
        r = r.next
    # print(r)