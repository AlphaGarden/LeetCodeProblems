"""

Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?


"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
"""
The fundamental thought of the solution :
Phase 1: Reverse the first half while finding the middle.
Phase 2: Compare the reversed first half with the second half.
"""
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        new_list = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            new_list, slow.next, slow = slow, new_list, slow.next
            """
            Now we construct a new reversed linked list for the first half part
            but the original Linked List will be 2 linked list
            e.g. 1->2->3->4->5->None
            And they will be spilt into 2 linked list:
            2->1->None
            4->5->None
            
            """
            # new_list, new_list.next, slow = slow, new_list, slow.next
        if fast:
            slow = slow.next
        while new_list and new_list.val == slow.val:
            new_list = new_list.next
            slow = slow.next
        return not new_list


if __name__ == '__main__':
    root = ListNode(1)
    node1 = ListNode(2)
    root.next = node1
    solution = Solution()
    print solution.isPalindrome(root)