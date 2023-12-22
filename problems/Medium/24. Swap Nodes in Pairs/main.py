# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# def Chain:
#     def __init__(self,head):
#         self.head = head
#         self.tail = head 
#         while self.tail.next:
#             self.tail = self.tail.next 
def print_list_node(head):
    r = ''
    tail = head
    while tail:
        r += f'{tail.val}->'
        tail = tail.next
    print(r)

class Solution:
    def swapPairs(self, head):
        l1 = head
        l2 = head.next if head else None
        l = ListNode()
        l = l2
        l_previous = ListNode()
        if not head or not head.next:
            return head
        while l1 and l2:
            print('l1.val: ',l1.val)
            print('l2.val: ',l2.val)
            print_list_node(l)
            l_previous.next = l2
            l3 = l2.next
            l4 = l3.next if l3 else None
            l2.next = l1 
            l1.next = l3 
            l_previous = l1 
            l1 = l3 
            l2 = l4
            print_list_node(l)
            # print('l1.val: ',l1.val)
            # print('l2.val: ',l2.val)
            # print('---')
            
        return l




if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    # f = ListNode(6)
    # a.next = b
    # b.next = c 
    # c.next = d
    # d.next = e
    # e.next = f
    # print_list_node(a)
    r = Solution().swapPairs(None)
    print_list_node(r)