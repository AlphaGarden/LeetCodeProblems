'''
Invert a binary tree.
     4
   /   \
  2     7
 / \   / \
1   3 6   9
to
     4
   /   \
  7     2
 / \   / \
9   6 3   1
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # Approach 1
        if not root: return None
        right_node = self.invertTree(root.right)
        left_node = self.invertTree(root.left)
        root.left = right_node
        root.right = left_node
        return root
    """
    The key point is that we should exhange each node in the subtree every time from the bottom to the top.
    step 1: 
     4
   /   \
  2     7
 / \   / \
1   3 6   9
    step 2:
     4
   /   \
  2     7
 / \   / \
3   1 9   6
    step 3:
     4
   /   \
  7     2
 / \   / \
9   6 3   1
    """

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
print solution.invertTree(root)
