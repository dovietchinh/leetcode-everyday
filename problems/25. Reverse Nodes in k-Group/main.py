# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        head = self 
        r = ""
        while head is not None:
            r += f"{head.val} -> "
            head = head.next
        return r
    
def create(list_value):
    head = ListNode()
    tail = head    
    for value in list_value:
        tail.next = ListNode(value)
        tail = tail.next
    return head.next

class Solution:
    def reverseKGroup(self, head, k: int):
        list_k = []
        temp = head 
        tail = head
        while(1):
            list_k.append(tail.val)
            if len(list_k) == k:
                for j in list_k[::-1]:
                    temp.val = j
                    temp = temp.next
                list_k = []
            tail = tail.next
            if tail is None:
                break
        return head
            

        


if __name__ == '__main__':
    a = [1,2,3,4,5,6,7,8,9,10]
    a = create(a)
    r = Solution().reverseKGroup(a,3)
    print('head: ',r)
