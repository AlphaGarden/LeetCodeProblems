"""
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# And the current_targets for current node are the pre_node_targets - pre_node.val
class Solution(object):
    def traverse(self, node, origin, targets):
        if node is None:
            return 0
        hit = 0
        for num in targets:
            if not (num - node.val): hit += 1
        targets = [origin] + [num - node.val for num in targets]
        return hit + self.traverse(node.left, origin, targets) + self.traverse(node.right, origin, targets)
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        return self.traverse(root, sum, [sum])

if __name__ == '__main__':
    # construct the binary tree
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

    # Initialize the solution
    solution = Solution()
    print solution.pathSum(root,3)
print  bool(0)