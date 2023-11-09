from typing import Optional
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        res = []
        res += self.inorderTraversal(root.left)
        res.append(root.val)
        res += self.inorderTraversal(root.right)
        return res


# root = [1,null,2,3]
# Output: [1,3,2]
root001 = TreeNode(1)
root001.left = TreeNode(None)
root001.right = TreeNode(2)
root001.right.left = TreeNode(3)

#print("Solution_Recursion")
#s = Solution()
#print(s.inorderTraversal(root001))

## Input: root = []
## Output: []
#root002 = TreeNode(None)

#print(s.inorderTraversal(root002))

## Input: root = [1]
## Output: [1]

#root003 = TreeNode(1)

#print(s.inorderTraversal(root003))

# Iterative solution
# Inorder Traversal using Stack:
# As we already know, recursion can also be implemented using stack. Here also we can use a stack to perform inorder traversal of a Binary Tree. Below is the algorithm for traversing a binary tree using stack.

# Create an empty stack (say S).
# Initialize the current node as root.
# Push the current node to S and set current = current->left until current is NULL
# If current is NULL and the stack is not empty then:
# Pop the top item from the stack.
# Print the popped item and set current = popped_item->right
# Go to step 3.
# If current is NULL and the stack is empty then we are done.


class Solution_Iteration:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Set current to root of binary tree
        # Set current to root of binary tree
        current = root

        # Initialize results, stack
        res, stack = [], []

        while True:
            # Reach the left most Node of the current Node
            
            if current is not None:
                print(current.val)
                # Place pointer to a tree node on the stack
                # before traversing the node's left subtree
                stack.append(current)

                current = current.left

            # BackTrack from the empty subtree and visit the Node
            # at the top of the stack; however, if the stack is
            # empty you are done
            elif stack:
                print("current is None")
                current = stack.pop()
                res.append(current.val)

                # We have visited the node and its left
                # subtree. Now, it's right subtree's turn
                current = current.right

            else:
                break

        return res


print("\n\n\nSolution_Iteration")
si = Solution_Iteration()

#print(si.inorderTraversal(root001))
#print(si.inorderTraversal(root002))
#print(si.inorderTraversal(root003))

# Constructed binary tree is
#             1
#          /    \
#         2      3
#       /  \    /  \
#      4    7  8    9
#    /  \          /  \
#   5    6        10    11 
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(7)
root.left.left.left = TreeNode(5)
root.left.left.right = TreeNode(6)
root.right.left = TreeNode(8)
root.right.right = TreeNode(9)
root.right.right.left  = TreeNode(10)
root.right.right.right = TreeNode(11)
print(si.inorderTraversal(root))