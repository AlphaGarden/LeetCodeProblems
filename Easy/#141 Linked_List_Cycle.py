"""
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Brute Force
        # we could try to traverse the list and put it in ino a list
        # every time we get a list node, we check whether this node is in the recording or not
        # if yes return True, else we get to the end of the single list
        # record = []
        # while(head):
        #     if head in record:
        #         return True
        #     else:
        #         record.append(head)
        #         head = head.next
        # return False

        # With hash table with time complexity with O(n) and space complexity O(n)

        # record = {}
        # while head:
        #     if record.has_key(head):
        #     else:
        #        return True
        #         record[head] = 1
        #         head = head.next
        # return False

        # Fast and slow runner
        if head is None: return False
        slow_node = head #(One step at a time)
        fast_node = head.next #(Two steps at a time)
        while slow_node != fast_node:
            if (fast_node is None) or (fast_node.next is None):
                return False
            slow_node = slow_node.next
            fast_node = fast_node.next.next
        return True

if __name__ == '__main__':
    # Construct solution Clas
    solution = Solution()
    # Construct Linked List
    root = ListNode(0)
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    tail = ListNode(4)
    root.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = tail
    # case 1: there is not cycle
    print solution.hasCycle(root)
    # case 2: there is no cycle
    tail.next = root
    print solution.hasCycle(root)