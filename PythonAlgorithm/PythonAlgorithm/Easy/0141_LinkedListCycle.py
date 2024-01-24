from typing import Optional
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    #Detect loop in a linked list using Hashing  
    #Time complexity: O(N)    
    #Auxiliary Space: O(N)  
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp = head
        s = set()
        while (temp):
            if temp in s:
                return True
            else:
                s.add(temp)
                temp = temp.next
        return False

    #Detect loop in a linked list using Floyd’s Cycle-Finding Algorithm  
    #Time complexity: O(N)    
    #Auxiliary Space: O(1)  
    def hasCycle_Floyd(self, head: Optional[ListNode]) -> bool:
        if head is None: return False
        if head.next is None: return False
        if head.next.next is None: return False
        slow = head.next
        fast = head.next.next
        while fast:
            if slow == fast:
                return True
            else:
                slow = slow.next
                if fast.next is None: return False 
                fast = fast.next.next
        return False



#Input: head = [3,2,0,-4], pos = 1
#Output: true

s =Solution()

nodeTemp = ListNode(0)
listNode1= ListNode(3)
nodeTemp = listNode1;
nodeTemp.next=ListNode(2)
nodeTemp=nodeTemp.next;
nodeTemp.next=ListNode(0)
nodeTemp=nodeTemp.next;
nodeTemp.next=ListNode(-4)
nodeTemp=nodeTemp.next;
nodeTemp.next=listNode1
print(listNode1.val,listNode1.next.val, listNode1.next.next.val, listNode1.next.next.next.val, listNode1.next.next.next.next.val )
print(s.hasCycle(listNode1))
print(s.hasCycle_Floyd(listNode1))



#Input: head = [1,2], pos = 0
#Output: true

listNode1= ListNode(1)
nodeTemp = listNode1;
nodeTemp.next=ListNode(2)
nodeTemp=nodeTemp.next;
nodeTemp.next=listNode1
print(s.hasCycle(listNode1))
print(s.hasCycle_Floyd(listNode1))


