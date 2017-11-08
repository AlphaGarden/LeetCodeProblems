'''
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.


Conclusion :

In the iterative version:
We could see that:
What we need to do first is to set up 2 variables to record the head of the list
Then. we keep comparing the node of l1 with the node of l2.
If the val of l1'head is smaller than the l2's:
    then we add the node of l1 in the the dummy node list(which is a kind of tricky way)
else:
    we add the node of l2 in the dummy node list
Finally we get the dummy head of the new list. And the next node will be the target list

In the recursive verion:
We should know that it is not easy to get the correct answer.
The basic strategy is :
    The base case is when one of them reach the end of the node:
        :return the remaining section of the other list
    if the value of l1 is smaller than l2:
        we set the next node of current node as the node which has smaller value
        between l1.next and l2, because we want to know the following node should come from
        which list, l1 one or l2. Therefore, we need to call the function itself to check.

        At this time. because we have operations on the node of l1, then it means we need
        to :return this node to the previous layer of the function
    else:
        we set the next node of current node as the node which has small value
        between l1 and l2.next, because we wonder the following node should come from which
        list, l1 or l2. Therefore, we need to call the function itsetl to check.

        At this time. because we have operations on the node of l2, then it means we need
        to :return this node to the previous layer of the function



'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    """
     :type l1: ListNode
     :type l2: ListNode
     :rtype: ListNode
     """
    # Iterative Version
    def mergeTwoLists(self, l1, l2):
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val<l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next
    # Recursive version
    def rec_mergeTwoLists(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2
        if l1.val<l2.val:
            l1.next = self.rec_mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next = self.rec_mergeTwoLists(l1,l2.next)
            return l2

    # In_place_Iteratively
    def in_place_mergeTwoLists(self,l1,l2):
        dummy = cur = ListNode(0)
        dummy.next = l1  # The first node of l1
        while l1 and l2:
            if l1.val < l2.val:  # When l1.val is smaller l2.val
                l1 = l1.next  # we skip the element
            else:  # When l1.val is larger than l2.val, insert the l2's element into l1
                nex = cur.next
                cur.next = l2
                temp = l2.next
                l2.next = nex
                l2 = temp
            cur = cur.next  # every time tracks the last number of ordered sequence of l1
        cur.next = l1 or l2
        return dummy.next

ln10 = ListNode(0)
ln11 = ListNode(1)
ln12 = ListNode(5)
ln10.next=ln11
ln11.next=ln12
ln20 = ListNode(2)
ln21 = ListNode(8)
ln22 = ListNode(9)
ln20.next=ln21
ln21.next=ln22

solution = Solution()
# print ln10.val
cur = solution.in_place_mergeTwoLists(ln10,ln20)
while(True):
    if cur != None:
        print cur.val
        cur = cur.next
    else:
        break