"""
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.equal_flag = True
        self.subtree_flag = False

    def equal(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if (s.left is None) and (t.left is not None):
            self.equal_flag = False
            return False
        if (s.left is not None) and (t.left is None):
            self.equal_flag = False
            return False
        if (s.right is None) and (t.right is not None):
            self.equal_flag = False
            return False
        if (s.right is not None) and (t.right is None):
            self.equal_flag = False
            return False
        if s.val != t.val:
            self.equal_flag = False
            return False
        if (s.left is None and t.left is None) and (s.right is None and t.right is None):
            return self.equal_flag
        if (s.left is None and t.left is None) and (s.right is not None and t.right is not None):
            return self.equal(s.right, t.right)
        if (s.left is not None and t.left is not None) and (s.right is None and t.right is None):
            return self.equal(s.left, t.left)
        self.equal(s.left, t.left)
        self.equal(s.right, t.right)
        return self.equal_flag

    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if s is None:
            return not(s and t)
        self.equal_flag = True
        if self.equal(s, t):
            self.subtree_flag = True
        self.isSubtree(s.left, t)
        self.isSubtree(s.right, t)
        return self.subtree_flag

if __name__ == '__main__':
    root = TreeNode(-4)
    n1 = TreeNode(5)
    n2 = TreeNode(2)
    n3 = TreeNode(9)
    n4 = TreeNode(0)
    n5 = TreeNode(3)
    n6 = TreeNode(7)
    n7 = TreeNode(1)
    n8 = TreeNode(6)
    n9 = TreeNode(8)
    root.right = n1
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n4.right = n7
    n6.left = n8
    n6.right = n9


    root2 = TreeNode(9)
    l12 = TreeNode(7)
    r12 = TreeNode(6)
    l1l22 = TreeNode(9501)
    root2.left = l12
    l12.left = r12
    l12.right = l1l22


    solution = Solution()
    #
    print solution.isSubtree(root, root2)
    # print solution.equal(root2, root2)
