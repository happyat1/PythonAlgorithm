from typing import Optional
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
            if root is None: return
            else:            
               queue = []
               queue.append (root)
               while (queue):
                   length = len(queue)
                   while length > 0:
                       node = queue.pop(0)
                       temp = node.left
                       node.left = node.right
                       if node.left is not None:queue.append(node.left)
                       node.right = temp
                       if node.right is not None:queue.append(node.right)
                       length-=1
            return root

    def invertTree_02(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None: return 
        temp = root.left
        root.left = root.right
        root.right = temp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


#Input: root = []
#Output: []
s =Solution()

root = None

print(s.invertTree_02(root))