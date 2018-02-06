"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?
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

        turtle = head.next
        bunny = head.next.next
        while turtle != bunny:
            turtle = turtle.next
            bunny = bunny.next.next
        # Check the entrance
        turtle = head
        while turtle != bunny:
            turtle = turtle.next
            bunny = bunny.next
        return turtle.val



if __name__ == '__main__':
    head = ListNode(0)
    node2 = ListNode(1)
    node3 = ListNode(2)
    node4 = ListNode(3)
    node5 = ListNode(4)
    head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = head
    solution = Solution()
    print solution.detectCycle(head)