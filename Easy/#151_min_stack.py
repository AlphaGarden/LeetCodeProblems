"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
"""

"""
The key solution is at the push() function
Every time we try to push a element into the list 
If we can keep the record of the current min value for this insertion,
then for everytime we get the minimum from the top of the stack.
"""
class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        cur_min = self.getMin()
        if cur_min == None or x < cur_min:
            cur_min = x
        self.q.append((x, cur_min))
    def pop(self):
        """
        :rtype: void
        """
        return self.q.pop()

    def top(self):
        """
        :rtype: int
        """
        if len(self.q) == 0:
            return None
        return self.q[len(self.q)-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.q) == 0:
            return None
        return self.q[len(self.q)-1][1]



        # Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(1)
# obj.pop()
# param_3 = obj.top()
param_4 = obj.getMin()
# print param_3
print(param_4)