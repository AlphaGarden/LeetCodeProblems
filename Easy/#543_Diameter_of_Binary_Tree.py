"""
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \
      4   5
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Solution:
# 1. First of all we need to understand how to get the depth of a binary treee
# 2. Assume that we get the max depth of a node's left child, and the max depth of a node's right
# child, then every time we record this 2 sum in a vaibl, named ans. when we return back to every
# node
# 3. we get a node's max depth (left depth + right depth + 1), which included the node itself
# 4. then we compare the previous number with the current ans, and record the relatively larger one
# 5. at the end we interate all the node and finally get the maximum path

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 1

        def depth(node):
            if node is None: return 0
            left = depth(node.left)
            right = depth(node.right)
            self.ans = max(self.ans, left + right + 1)
            return max(left, right) + 1
        depth(root)
        return self.ans - 1


# Tree Construction
root = TreeNode(1)
l1 = TreeNode(2)
r1 = TreeNode(3)
l1l2 = TreeNode(4)
l1r2 = TreeNode(5)
r1l2 = TreeNode(6)
r1r2 = TreeNode(7)
root.left = l1
root.right = r1
l1.left = l1l2
l1.right = l1r2
r1.left = r1l2
r1.right = r1r2

solution = Solution()
print(solution.diameterOfBinaryTree(root))