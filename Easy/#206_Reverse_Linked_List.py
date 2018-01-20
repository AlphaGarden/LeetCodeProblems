'''
Reverse a singly linked list.
A linked list can be reversed either iteratively or recursively. Could you implement both?
'''

"""
Be careful that the the variable scope of the nested function.
We should understand  that we are not allowed to access the outer variable in python 2.7.
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    # Iterative way
    # def reverseList(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: ListNode
    #     """
    #     prev = None
    #     curr = head
    #     while curr:
    #         temp_node = curr.next
    #         curr.next = prev
    #         prev = curr
    #         curr = temp_node
    #     return prev

    # Recursive way
    def __init__(self):
        self.start = None
        # For the nested function of python 2.7, It is not allowed to access the
        # outer variable of the outer function
        # Be careful
    def reverseList(self, head):

        if not head:
            return head

        def rev(node):
            if node.next is None:
                self.start = node
                return node
            (rev(node.next)).next = node
            return node

        rev(head).next = None
        return self.start


solution = Solution()

root = ListNode(0)
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)

root.next = l1
l1.next = l2
l2.next = l3
l3.next = l4

temp = solution.reverseList(root)
while (temp):
    print temp.val
    temp = temp.next
