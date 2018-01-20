'''
Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is
changed to the original key plus sum of all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13
'''

"""
The key point solution is using the reversed in - order traverse  method to solve the problem. 
Easy and staright forward.
But you should know how we do in - order traverse   method for binary search tree (BST)
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.total = 0

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is not None:
            self.convertBST(root.right)
            self.total += root.val
            root.val = self.total
            self.convertBST(root.left)
        return root


# Tree Construction
root = TreeNode(6)
l1 = TreeNode(3)
r1 = TreeNode(8)
l1l2 = TreeNode(1)
l1r2 = TreeNode(4)
r1r2 = TreeNode(9)
r1r2r3 = TreeNode(10)
root.left = l1
root.right = r1
l1.left = l1l2
l1.right = l1r2
r1.left = r1r2
r1r2.right = r1r2r3

solution = Solution()
print solution.convertBST(root)
