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
    def mergeKLists(self, lists):
        head = ListNode()
        tail = head 
        while(1):
            value,index = search_min_in_list(lists)
            if value is None:
                break
            tail.next = ListNode(value)
            tail = tail.next
            lists[index] = lists[index].next
        return head.next            
                

def search_min_in_list(list):
    value = None
    index = None
    for i,element in enumerate(list):
        if element is None:
            continue
        if value is None:
            value = element.val
            index = i
        else:
            if value > element.val:
                value = element.val
                index = i
    return value,index



if __name__ == '__main__':
    a = [[1,4,5],[1,3,4],[2,6]]
    a = [[0,2,5]]
    a = [create(x) for x in a]
    r = Solution().mergeKLists(a)
    print('r: ',r)