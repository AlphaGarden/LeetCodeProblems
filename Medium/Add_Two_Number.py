#
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        l1CurrentNode = l1
        l2CurrentNode = l2
        result = []
        add = 0
        while(l1CurrentNode!= None or l2CurrentNode!= None):
            if(l1CurrentNode==None):
                while(l2CurrentNode != None):
                    # Come to the end of l2
                    tempNum1 = l2CurrentNode.val + add
                    add = tempNum1/10
                    result.append(tempNum1 % 10)
                    if (l2CurrentNode.next == None):
                        if (add == 1):
                            result.append(1)
                            return result
                    l2CurrentNode = l2CurrentNode.next
                return result
            if(l2CurrentNode==None):
                while(l1CurrentNode!=None):
                    tempNum2 = l1CurrentNode.val + add
                    add = tempNum2/10
                    result.append(tempNum2 % 10)
                    # Come to the end of l1
                    if(l1CurrentNode.next == None):
                        if(add == 1):
                            result.append(1)
                            return result
                    l1CurrentNode = l1CurrentNode.next
                return result
            temp = l1CurrentNode.val + l2CurrentNode.val + add
            result.append(temp%10)
            add = temp/10
            if(l1CurrentNode.next == None and l2CurrentNode.next ==None):
                if (add == 1):
                    result.append(1)
            l1CurrentNode = l1CurrentNode.next
            l2CurrentNode = l2CurrentNode.next
        return result


l1 = ListNode(3)
l1.next = ListNode(7)
# l1.next.next = ListNode(3)
l2 = ListNode(9)
l2.next = ListNode(2)
# l2.next.next = ListNode(4)
test = Solution()
result = test.addTwoNumbers(l1,l2)
print (result)
# while(testNode.next!=None):
#     print ('['+str(testNode.val)+'->')
#     testNode = testNode.next
# print (']')
