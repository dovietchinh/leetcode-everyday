from typing import *
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode()
        ptr = root 
        l = list1 
        while l:
            print('list1: ',l.val)
            l = l.next
        l = list2
        while l:
            print('list2: ',l.val)
            l = l.next
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val < list2.val:
            ptr.val = list1.val
            list1 = list1.next
        else:
            ptr.val = list2.val
            list2 = list2.next
        while list1 or list2:
            if list1 is None:
                ptr.next = list2
                list2 = list2.next
                ptr = ptr.next
                continue 
            if list2 is None:
                ptr.next = list1
                list1 = list1.next
                ptr = ptr.next
                continue
            if list1.val < list2.val:
                ptr.next = list1
                list1 = list1.next
                ptr = ptr.next
                continue 
            else:
                ptr.next = list2
                list2 = list2.next
                ptr = ptr.next
                continue
            
        return root
                
if __name__ == '__main__':
    root = Solution().mergeTwoLists(ListNode(1,ListNode(2,ListNode(4))),ListNode(1,ListNode(3,ListNode(4))))
    while root:
        print("root.val: ",root.val)
        root = root.next