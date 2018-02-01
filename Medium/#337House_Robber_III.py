"""
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:
     3
    / \
   2   3
    \   \
     3   1
Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:
     3
    / \
   4   5
  / \   \
 1   3   1
Maximum amount of money the thief can rob = 4 + 5 = 9.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
        def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        return max(self.dfs(root), (self.dfs(root.left) + self.dfs(root.right)))
    # pre_order
    def dfs(self,root):
        if not root: return 0
        if not root.left and not root.right:
            return root.val
        if not root.left or not root.right:
            return root.val + self.dfs((root.left or root.right).left) + self.dfs((root.left or root.right).right)
        return root.val+ self.dfs(root.left.left) + self.dfs(root.left.right) + self.dfs(root.right.left) + self.dfs(root.right.right)
    def basic_dfs(self,root):
if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(3)
    l1 = TreeNode(2)
    r1 = TreeNode(3)
    l1r2 = TreeNode(3)
    r1r2 = TreeNode(1)
    root.left = l1
    root.right = r1
    l1.right = l1r2
    r1.right = r1r2
    solution.dfs(root)
