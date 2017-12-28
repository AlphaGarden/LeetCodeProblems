'''
Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

Example 1:
Input: 
	Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  
Output: 
Merged tree:
	     3
	    / \
	   4   5
	  / \   \ 
	 5   4   7
Note: The merging process must start from the root nodes of both trees.
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        # At the base case when both of them are empty tree
        if not t1 and not t2: return None
        # root = TreeNode(t1.val if t1 else 0 + t2.val if t2 else 0)
        root = TreeNode((t1.val if t1 else 0) + (t2.val if t2 else 0))
        root.left = self.mergeTrees(t1 and t1.left, t2 and t2.left)
        root.right = self.mergeTrees(t1 and t1.right, t2 and t2.right)
        # Out of recursive limitation
        # root.left = self.mergeTrees(t1.left and t1 ,t2.left and t2)
        # root.right = self.mergeTrees(t1.right and t1,t2.right and t2)
        return root

    """
     Attention: for usage of 'and' operator in python
     Python does have some additional functionality in its boolean operators.
     Knowing these helps you write better code.
     Operators are short circuiting. Consider the statement a and b: 
     if a is not True, the value of b does not matter for the result.
     Thus, Python will not bother evaluating b at all.
     This is useful if b is undefined without a. 
     For example, consider an optional dictionary argument. 
     You can test whether it is set, and test one of its key within one expression - the later would be an invalid operation otherwise.
     """

    """
    for 
    """
