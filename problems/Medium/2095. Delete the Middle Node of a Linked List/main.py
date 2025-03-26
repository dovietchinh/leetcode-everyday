# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        if head.next is None:
            return None
        if head.next.next is None:
            head.next = None
            return head 
        pre_slow = None
        slow = head 
        fast = head 
        while fast.next:
            pre_slow = pre_slow.next if pre_slow else head
            slow = slow.next
            fast = fast.next.next if fast.next.next else fast.next
        pre_slow.next = slow.next
        return head 
