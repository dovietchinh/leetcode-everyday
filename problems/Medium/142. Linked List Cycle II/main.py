from typing import *
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def print(self):
        print(self.val, end='->')
        if self.next:
            self.next.print()
        else:
            print()

def create_list_node(nums):
    if len(nums) == 0:
        return None 
    head = ListNode(nums[0])
    p = head 
    for i in nums[1:]:
        p.next = ListNode(i)
        p = p.next
    return head 

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None 
        if head.next.next is head:
            return head
        # two pointers technique
        p1 = head 
        p2 = head 
        count_meet = 0
        while True:
            print('p1.val, p2.val ',p1.val, p2.val)
            if p2 is None or p2.next is None:
                return None
            if p2 is p1:
                count_meet += 1
                if count_meet >1:
                    p1 = head 
                    break
            p1 = p1.next 
            p2 = p2.next.next if p2.next else None 
        while p1 is not p2:
            print('p1.val, p2.val ',p1.val, p2.val)
            p1 = p1.next 
            p2 = p2.next
        return p1
        


        
            



if __name__ == '__main__':
    nums = [ListNode(0),ListNode(1),ListNode(2),ListNode(3),ListNode(4),ListNode(5),ListNode(6)] 
    nums[0].next = nums[1]
    nums[1].next = nums[2]
    nums[2].next = nums[3]
    nums[3].next = nums[4]
    nums[4].next = nums[5]
    nums[5].next = nums[6]
    nums[6].next = nums[0]
    # nums[7].next = nums[2]
    # print('nums[3].val: ',nums[3].val)
    head = nums[0]
    r = Solution().detectCycle(head)
    print('r: ',r)
    print(r.val)
    # print(r.val)
    
    # head.print()
    