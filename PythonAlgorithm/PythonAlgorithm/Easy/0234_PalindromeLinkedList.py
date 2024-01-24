
from typing import Optional
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
       stack = []
       temp = head
       while temp is not None:
           stack.append(temp)
           temp = temp.next
       while head is not None:
            node = stack.pop()
            if head.val == node.val :
               head = head.next
            else:
                return False
       return True

#Input:head = [1,2]
#Output: false

s =Solution()


head1=ListNode(1)
head1.next=ListNode(2)
print(s.isPalindrome(head1))

#Input: head = [1,2,2,1]
#Output: true

head1=ListNode(1)
head1.next=ListNode(2)
head1.next.next=ListNode(2)
head1.next.next.next=ListNode(1)
print(s.isPalindrome(head1))