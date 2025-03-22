from typing import *
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def print(self):
        print(self.val,'->')
        if self.next:
            self.next.print()
        else:
            print()

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #handle edge case
        if head is None or head.next is None:
            return head
        arrayNode = []
        p = head 
        while p:
            arrayNode.append(p)
            p = p.next
        
        arrayNode.sort(key=lambda x:x.val)
        for i in arrayNode:
            print(i.val)
        head = arrayNode[0]
        for i in range(len(arrayNode)-1):
            arrayNode[i].next = arrayNode[i+1]
        arrayNode[-1].next = None 
        return head
        
        
    def sortArray(nums):
        
        


if __name__ == '__main__':
    head = ListNode(0,ListNode(1,ListNode(5,ListNode(3,ListNode(4)))))
    r = Solution().sortList(head)
    print('r: ',r)