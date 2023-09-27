from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


#Input: root = [3,9,20,null,null,15,7]
#Output: 3
root001 = TreeNode(3)
root001.left = TreeNode(9)
root001.right = TreeNode(20)
root001.left.left = None
root001.left.right = None
root001.right.left = TreeNode(15)
root001.right.right = TreeNode(7)

#Input: root = [1,null,2]
#Output: 2
root002 = TreeNode(1)
root002.left = None
root002.right = TreeNode(2)


class Solution(object):
    def maxDepth(self, root):
        if root is None: return 0
        lL = self.maxDepth(root.left)
        lR = self.maxDepth(root.right)
        if lL > lR:
            return lL+1
        else:
            return lR+1
    
s = Solution()
print(s.maxDepth(root001))
print(s.maxDepth(root002))


class Solution_Iteration:
    def maxDepth(self, root):
        # Base Case
        if root is None:
            return 0
   
        # Create an empty queue for level order traversal
        q = []
   
        # Enqueue Root and initialize height
        q.append(root)
        height = 0
   
        # Loop while queue is not empty
        while q:
   
            # nodeCount (queue size) indicates number of nodes
            # at current level
            nodeCount = len(q)
   
            # Dequeue all nodes of current level and Enqueue all
            # nodes of next level
            while nodeCount > 0:
                node = q.pop(0)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                nodeCount -= 1
            height += 1
   
        return height

print("\n\n\nSolution_Iteration")
s_iteration = Solution_Iteration()
print(s_iteration.maxDepth(root001))
print(s_iteration.maxDepth(root002))