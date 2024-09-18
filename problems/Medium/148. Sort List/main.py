from typing import *
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def partition(root,low,high):
            pivot = root.val 
            ptr = root 
            ptr2 = ptr
            while ptr:
                ptr = ptr.next 
                if ptr.val > pivot:
                    ptr2 = ptr2.next




if __name__ == '__main__':
    head = ListNode(4,ListNode(2,ListNode(1,ListNode(3))))
    r = Solution().sortList(head)
    while r:
        print(r.val)
        r = r.next
    head = ListNode(-1,ListNode(5,ListNode(3,ListNode(4,ListNode(0)))))
    r = Solution().sortList(head)
    while r:
        print(r.val)
        r = r.next
    head = None
    r = Solution().sortList(head)
    while r:
        print(r.val)
        r = r.next
    head = ListNode(1)
    r = Solution().sortList(head)
    while r:
        print(r.val)
        r = r.next
    head = ListNode(2,ListNode(1))
    r = Solution().sortList(head)
    while r:
        print(r.val)
        r = r.next
    head = ListNode(4,ListNode(19,ListNode(14,ListNode(5,ListNode(-3,ListNode(1,ListNode(8,ListNode(8,ListNode(12,ListNode(7,ListNode(6,ListNode(9,ListNode(11,ListNode(15,ListNode(16,ListNode(17,ListNode(18,ListNode(13,ListNode(10,ListNode(2,ListNode(3,ListNode(0,ListNode(20,ListNode(21,ListNode(22,ListNode(23,ListNode(24,ListNode(25,ListNode(26,ListNode(27,ListNode(28,ListNode(29,ListNode(30,ListNode(31,ListNode(32,ListNode(33,ListNode(34,ListNode(35,ListNode(36,ListNode(37,ListNode(38,ListNode(39,ListNode(40,ListNode(41,ListNode(42,ListNode(43,ListNode(44,ListNode(45,ListNode(46,ListNode(47,ListNode(48,ListNode(49,ListNode(50,ListNode(51,ListNode(52,ListNode(53,ListNode(54,ListNode(55,ListNode(56,ListNode(57,ListNode(58,ListNode(59,ListNode(60,ListNode(61,ListNode(62,ListNode(63,ListNode(64,ListNode(65,ListNode(66,ListNode(67,ListNode(68,ListNode(69,ListNode(70,ListNode(71,ListNode(72,ListNode(73,ListNode(74,ListNode(75))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
    r = Solution().sortList(head)
    while r:
        print(r.val)
        r = r.next