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
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head 
        fast = head 
        pre_slow = None
        while fast:
            # print('pre_slow: ',pre_slow.val if pre_slow else None)
            # print('slow: ',slow.val if slow else None)
            # print('fast: ',fast.val if fast else None)
            # reverse direction if a half linked-list
            fast = fast.next.next
            next_slow = slow.next
            slow.next = pre_slow
            pre_slow = slow
            slow = next_slow
            
        results = float('-inf')
        while slow:
            total = slow.val + pre_slow.val
            results = max(results,total)
            slow = slow.next
            pre_slow = pre_slow.next
        return results
            
if __name__ == '__main__':
    head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,ListNode(6))))))
    head.print()
    r = Solution().pairSum(head)
    print('r: ',r)