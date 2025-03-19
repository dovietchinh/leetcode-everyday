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
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # handle edge case
        if head is None:
            return 
        if head.next is None:
            return 
        if head.next.next is None:
            return head
        p1 = head 
        p2 = head 
        p2_pos = 0
        while p2.next:
            p1 = p1.next 
            if p2.next is not None:
                if p2.next.next is None:
                    p2 = p2.next 
                    p2_pos += 1
                    break 
                p2 = p2.next.next
                p2_pos += 2
            else:  # p2 reach final node , there are odd numbers of nodes in linked-list
                break 
        if p2_pos % 2 == 0: # p1 point to center 
            p2 = inverse_linked_list(p1)
        else: # p1.next poin to center
            p2 = inverse_linked_list(p1)
        p = head 
        while p.next is not p1:
            p = p.next 
        p.next = None
            
        

        print('p1: ')
        head.print()
        print('p2: ')
        p2.print()

        p = merge_linked_list(head,p2)
        print('p: ')
        p.print()
        return head
def merge_linked_list(head1,head2):
    p1 = head1
    p2 = head2
    while p1 and p2:
        temp = p1.next if p1 else None 
        temp2 = p2.next if p2 else None
        if temp is None and temp2 is None: 
            p1.next = p2 
            p1 = temp 
            p2 = temp2 
            break 
        elif temp is None and temp2 is not None: 
            p1.next = p2 
            break 
        elif temp is not None and temp2 is not None: 
            p1.next = p2 
            p1 = temp 
            p2.next = temp 
            p2 = temp2 
        elif temp is not None and temp2 is  None: 
            p1.next = p2 
            p2.next = temp 
            break 
    return head1 


        

def inverse_linked_list(head):
    p1 = head 
    p2 = head.next 
    p3 = head.next.next if p2 else None 
    p1.next = None
    if p3 is None:
        p2.next = p1 
        return p2
    while p3:
        p2.next = p1 
        p1 = p2 
        p2 = p3
        p3 = p3.next
    if p2:
        p2.next = p1 
        p1 = p2

    return p1


        
        # if even node: p2 point to final node, p1 pointe to center - 0.5  # p1.next is centers
        # if odd node: p2 point to final node, p1 pointe to center  # p1 is center

if __name__ == '__main__':
    head = ListNode(1,ListNode(2))
    # head2 = ListNode(11,ListNode(12,ListNode(13,ListNode(14))))
    r = Solution().reorderList(head)
    # h = merge_linked_list(head,head2)
    # h.print()
    # head.print()
    # p = inverse_linked_list(head)
    # p.print()

        

            
        