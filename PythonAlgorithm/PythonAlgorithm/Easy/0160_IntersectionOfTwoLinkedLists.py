from ast import If
from typing import Optional
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode):
            c1=self.getCount(headA)
            c2=self.getCount(headB)
            if c1 > c2:
                d = c1 - c2
                return self._getIntersectionNode(d, headA,headB)
            else:
                d = c2 - c1
                return self._getIntersectionNode(d, headB,headA)



    def getCount(self,node):
        cur=node
        count=0
        while cur is not None:
            count+=1
            cur=cur.next
        return count

    def _getIntersectionNode(self,d,head1,head2):
        current1=head1
        current2=head2
        for i in range (d):
            current1 = current1.next
        print("start:"+ str(current1.val))

        while current1 is not None:
            print("current1:"+str(current1.val))
            print("current2:"+str(current2.val))
            if  current1 is current2:
                return current1
            else: 
                current1 =current1.next                
                current2 =current2.next
                
        return None

    def getIntersectionNode_02(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        nodeA = headA
        nodeB = headB
        candidate = None
        listAExtended = False
        listBExtended = False
        while True: 
              print ("nodeA")
              print (nodeA)
              print (nodeA.val)
              print ("nodeB")
              print (nodeB)
              print (nodeB.val)
             
              if candidate is not None:
                 print ("candidate")
                 print (candidate.val)

              if nodeA is nodeB: 
                  if candidate is None:
                     candidate = nodeA # only update candidate if the previous node is not candidate
              else: candidate = None

              if nodeA.next is not None: nodeA = nodeA.next
              elif nodeA.next is None and not listAExtended: 
                  nodeA = headB
                  listAExtended = True
              else: break

              if nodeB.next is not None: nodeB = nodeB.next
              elif nodeB.next is None and not listBExtended: 
                  nodeB = headA
                  listBExtended = True
              else: break
              
        return candidate


s =Solution()

common=ListNode(8)

head1=ListNode(4)
head1.next=ListNode(1)
head1.next.next=common
head1.next.next.next=ListNode(4)
head1.next.next.next.next=ListNode(5)

head2=ListNode(5)
head2.next=ListNode(6)
head2.next.next=ListNode(1)
head2.next.next.next=common
head2.next.next.next.next=ListNode(8)
head2.next.next.next.next.next=ListNode(4)
head2.next.next.next.next.next.next=ListNode(5)

#print(s.getIntersectionNode(head1,head2))
print(s.getIntersectionNode_02(head1,head2))