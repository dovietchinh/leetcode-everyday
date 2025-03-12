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


class Solution:
    def swapPairs(self,head):
        pre = None 
        cur = head 
        nex = cur.next  if cur else None

        while nex:
            temp = nex.next
            cur.next = temp
            nex.next = cur 
            if pre:
                pre.next = nex
            else:
                head = nex
            pre = cur 
            cur = temp 
            nex = cur.next if cur else None 
        return head

if __name__ == '__main__':
    # a = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,ListNode(6))))))
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    f = ListNode(6)
    g = ListNode(7)
    # h = ListNode(8)
    a.next = b
    b.next = c 
    c.next = d
    d.next = e
    e.next = f
    f.next = g
    # g.next = h

    print_list_node(a)
    # print_list_node(r)
    r = Solution().swapPairs(None)
    print_list_node(r)