'''
Serialization is the process of converting a data structure or object into a sequence of bits
so that it can be stored in a file or memory buffer, 
or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree.
There is no restriction on how your serialization/deserialization algorithm should work. 
You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized 
to the original tree structure.

For example, you may serialize the following tree

    1
   / \
  2   3
     / \
    4   5
as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes a binary tree. 
You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
Note: Do not use class member/global/static variables to store states. 
Your serialize and deserialize algorithms should be stateless.
'''


# This is soultion is kind of shit!!!!


# Definition for a binary tree node.
from Queue import Queue
from collections import deque

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        SYMBOL_SEPARATOR = ' '
        SYMBOL_NONE = 'X'
        if root == None : return ""
        queue = Queue() # If maxsize is <= 0, the queue size is infinite
        queue.put(root)
        ans_str = ''
        while not queue.empty():
            cur_node = queue.get()
            # print cur_node
            ans_str += SYMBOL_SEPARATOR+(str(cur_node.val) if cur_node else SYMBOL_NONE)
            if cur_node:
                queue.put(cur_node.left)
                queue.put(cur_node.right)
        return ans_str[1:]

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        SYMBOL_SEPARATOR = ' '
        SYMBOL_NONE = 'X'
        if data == "": return None
        queue = Queue()
        value_list = data.split(SYMBOL_SEPARATOR)
        root = TreeNode(value_list[0])
        queue.put(root)
        index = 1
        while index < len(value_list):
            parent = queue.get()
            if value_list[index] != SYMBOL_NONE:
                left = TreeNode(value_list[index])
                parent.left = left
                queue.put(left)
            index += 1
            if value_list[index] != SYMBOL_NONE:
                right = TreeNode(value_list[index])
                parent.right = right
                queue.put(right)
            index += 1
        return root

        # Your Codec object will be instantiated and called as such:
        # codec = Codec()
        # codec.deserialize(codec.serialize(root))

root1 = TreeNode(1)
l1 = TreeNode(2)
l2 = TreeNode(3)
r2 = TreeNode(4)
r1 = TreeNode(5)

# root.left = l1
# root.right = r1
# l1.left = l2
# l1.right = r2

root2 = TreeNode(1)
root2.left = l1
root2.right = l2
l2.left = r2
l2.right = r1


codec = Codec()
# codec.deserialize(codec.serialize(root))
# print codec.serialize(root2)
print (codec.deserialize(codec.serialize(root2)))