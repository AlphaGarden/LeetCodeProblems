'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
'''


# Definition for a binary tree node.
from Queue import Queue


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        # try to use bfs to iterate the binary tree, and use a list to store the node of each level of the tree,
        # then judge if they are symmetric
        """
        :type root: TreeNode
        :rtype: bool
        """
        # The method of using the two Queue
        # The case when the root is None
        if root == None: return True
        # current level queue
        queue1 = Queue()
        # next level queue
        queue2 = Queue()
        queue1.put(root)
        temp = []
        while not queue1.empty():
            cur_node = queue1.get()
            temp.append(cur_node.val if cur_node else None)
            if cur_node:
                queue2.put(cur_node.left)
                queue2.put(cur_node.right)
            if queue1.empty() and not queue2.empty():
                if temp != temp[::-1] : return False
                temp = []
                while not queue2.empty():
                    queue1.put(queue2.get())
        return True

# Contruct the Node for the tree
root = TreeNode(1)
l1 = TreeNode(2)
r1 = TreeNode(2)
l1l1 = TreeNode(3)
l1r1 = TreeNode(4)
r1l1 = TreeNode(4)
r1r2 = TreeNode(3)

# Construct the tree
root.left = l1
root.right = r1
l1.left = l1l1
l1.right = l1r1
r1.left = r1l1
r1.right = r1r2

# Test
solution = Solution()
print solution.isSymmetric(root)
