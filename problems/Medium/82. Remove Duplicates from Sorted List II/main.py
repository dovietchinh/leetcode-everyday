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

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = None
        p1 = head 
        p2 = head.next if p1 else None  
        count_value = 1
        while p2:
            print('cur:', cur.val if cur else None, end='    ')
            print('p1:', p1.val if p1 else None, end='    ')
            print('p2:', p2.val if p2 else None)
            if p2.val == p1.val:
                count_value += 1
                p2 = p2.next 
            else:  # p2 != p1
                if count_value == 1:
                    if cur is None:
                        head = p1 
                        cur = p1 
                    else:
                        cur.next = p1 
                        cur = p1 
                    p1 = p2
                    p2 = p2.next if p1 else None 
                    count_value = 1
                else:
                    p1 = p2 
                    p2 = p2.next 
                    count_value = 1
        if count_value == 1:
            if cur:
                cur.next = p1 
                cur = p1
            else: # cur is None 
                head = p1 
                cur = p1 
        if cur:
            cur.next = None
        else:
            head = None
        # head.print()
        return head


    
            



if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4,ListNode(5)))))))
    head = ListNode(1, ListNode(1))
    # head = ListNode(1, ListNode(1, ListNode(1, ListNode(2, ListNode(3)))))
    head = Solution().deleteDuplicates(head)
    # while head:
    #     print(head.val)
    #     head = head.next

