"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:
    2
   / \
  1   3
Binary tree [2,1,3], return true.
Example 2:
    1
   / \
  2   3
Binary tree [1,2,3], return false.

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """



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
