'''
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.

Conclusion:
The key part of doing such a problem is to keep the trap the nth node from the end of the
list.

But we can do it by setting up a slide window to do so
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        dummy = target_node = current = ListNode(0)
        current.next = head
        count = 0
        while current != None:
            if count > n :
                target_node = target_node.next
            current = current.next
            count += 1
        target_node.next = target_node.next.next
        return dummy.next
head = ListNode(1)
second_node = ListNode(2)
third_node = ListNode(3)
fourth_node = ListNode(4)
fifth_node = ListNode(5)
head.next =  second_node
second_node.next = third_node
third_node.next = fourth_node
fourth_node.next = fifth_node
solution = Solution()
start = solution.removeNthFromEnd(head,1)
while start != None:
    print (start.val)
    start = start.next