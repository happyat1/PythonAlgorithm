from typing import Optional
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        curr = head
        while curr is not None:
            temp = curr.next
            curr.next = pre
            pre = curr
            curr = temp 
            print(pre.val)
        return pre


#Input: head = [1,2,3,4,5]
#Output: [5,4,3,2,1]

s =Solution()
head = ListNode(1)
head.next =ListNode(2)
head.next.next =ListNode(3)
head.next.next.next =ListNode(4)
head.next.next.next.next =ListNode(5)

print(s.reverseList(head).val)