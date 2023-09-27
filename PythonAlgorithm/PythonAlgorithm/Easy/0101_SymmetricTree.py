
from pickle import FALSE
from typing import List

#Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#Input: root = [1,2,2,3,4,4,3]
#Output: True
root001 = TreeNode(1)
root001.left = TreeNode(2)
root001.right = TreeNode(2)
root001.left.left = TreeNode(3)
root001.left.right = TreeNode(4)
root001.right.left = TreeNode(4)
root001.right.right = TreeNode(3)

#Input: root = [1,2,2,null,3,null,3]
#Output: False
root002 = TreeNode(1)
root002.left = TreeNode(2)
root002.right = TreeNode(2)
root002.left.left = None
root002.left.right = TreeNode(3)
root002.right.left = None
root002.right.right = TreeNode(3)

class Solution(object):
    def isSymmetric(self, root):
        return isMirror(root,root)

def isMirror(node1,node2):
    if node1 ==None and node2 ==None: return True
    if node1 is not None and node2 is not None:
       if node1.val == node2.val:
          return isMirror(node1.left, node2.right) and isMirror(node1.right, node2.left)
       else: return False

    return False

s = Solution()
print(s.isSymmetric(root001))
print(s.isSymmetric(root002))


class Solution_Iteration:
    def isSymmetric(self, root):
        if root is None: return True
        stack = []
        stack.append(root)
        stack.append(root)
        while stack:
            node1 = stack.pop()
            node2 = stack.pop()
            if node1 is None and node2 is None:
               continue   
            elif node1 is not None and node2 is not None:
                if node1.val == node2.val:
                    stack.append(node1.left)
                    stack.append(node2.right)
                    stack.append(node1.right)
                    stack.append(node2.left)
                else: return False
            else: return False
        return True

print("\n\n\nSolution_Iteration")
s_iteration = Solution_Iteration()
print(s_iteration.isSymmetric(root001))
print(s_iteration.isSymmetric(root002))