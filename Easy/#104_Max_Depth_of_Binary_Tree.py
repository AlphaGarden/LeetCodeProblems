'''
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        left_depth = self.maxDepth(root.left) + 1
        right_depth = self.maxDepth(root.right) + 1
        return max(left_depth,right_depth)


# Tree Construction
root = TreeNode(1)
l1 = TreeNode(2)
r1 = TreeNode(2)
l1l2 = TreeNode(3)
l1r2 = TreeNode(3)
r1r2 = TreeNode(4)
r1r2r3 = TreeNode(5)
root.left = l1
root.right = r1
l1.left = l1l2
l1.right = l1r2
r1.left = r1r2
r1r2.right = r1r2r3

# Test
solution = Solution()
print solution.maxDepth(root)