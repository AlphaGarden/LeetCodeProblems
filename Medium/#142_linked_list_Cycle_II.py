"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?
"""

"""
Solution:
The basic idea is about Two points.
We have a slow point and a fast point
And If there is circle in the linked list
Then here will exist the case that the fast point catches up with the slow point eventually.
After they get to the intersection point.
proof by mathematics 
If will traverse the list from the beginning and the intersection point by two points step by step,
and finally they will meet each other at the entrance of loop again.

"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return None
        turtle = head.next
        bunny = head.next.next
        while turtle != bunny:
            if not bunny or not bunny.next:
                return None
            turtle = turtle.next
            bunny = bunny.next.next
        # Check the entrance
        turtle = head
        while turtle != bunny:
            turtle = turtle.next
            bunny = bunny.next
        return turtle

if __name__ == '__main__':
    head = ListNode(0)
    node2 = ListNode(1)
    node3 = ListNode(2)
    node4 = ListNode(3)
    node5 = ListNode(4)
    head.next = head

    solution = Solution()
    print solution.detectCycle(head)