
from pickle import FALSE
from typing import List

#Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#Input: root = [3,9,20,null,null,15,7]
#Output: [[3],[9,20],[15,7]]
root001 = TreeNode(3)
root001.left = TreeNode(9)
root001.right = TreeNode(20)
root001.right.left = TreeNode(15)
root001.right.right = TreeNode(7)

#Input: root = [1]
#Output: [[1]]
root002 = TreeNode(1)

class Solution(object):
    def levelOrder(self, root):
        if root is None: return []
        res = []
        queue =[root]
        nodesCount_level = 1
        nodesCount_Nextlevel = 0
        nodes_currentlevel =[]

        while queue:
              node = queue.pop(0)
              nodes_currentlevel.append(node.val)
              if node.left is not None:
                  queue.append(node.left)
                  nodesCount_Nextlevel += 1
              if node.right is not None:
                  queue.append(node.right)
                  nodesCount_Nextlevel += 1

              nodesCount_level -=1
              if nodesCount_level == 0:
                res.append(nodes_currentlevel)
                nodesCount_level = nodesCount_Nextlevel
                nodesCount_Nextlevel =0
                nodes_currentlevel =[]

        return res

s = Solution()
print(s.levelOrder(root001))
print(s.levelOrder(root002))

