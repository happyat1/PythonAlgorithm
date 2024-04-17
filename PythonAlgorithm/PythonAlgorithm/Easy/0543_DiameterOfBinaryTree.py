
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:   return 0
 
        # Get the height of left and right sub-trees
        lheight = self.height(root.left)
        rheight = self.height(root.right)
    
        ldiameter = self.diameterOfBinaryTree(root.left)
        rdiameter = self.diameterOfBinaryTree(root.right)
    
        return max(lheight + rheight, max(ldiameter, rdiameter))

    def height(self,node): 
        if node is None:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    def diameterOfBinaryTree_fast(self, root: Optional[TreeNode]) -> int:
        def depth(node):
            if node is None:
                return 0
            left_depth = depth(node.left)
            right_depth = depth(node.right)
            # Update diameter while traversing the tree
            nonlocal diameter
            diameter = max(diameter, left_depth + right_depth)
            # Return the depth of the current node
            return 1 + max(left_depth, right_depth)

        diameter = 0
        depth(root)
        return diameter