# coding=utf-8
'''
Requirement:
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

Conclusion:
    *sets --- Unordered collections of unique elements
    *lists--- ordered collections of elements
1. Sets can't contain duplicates
2. Sets are unordered
3. In order to find an element in a set, a has lookup is used(which is why sets are unordered).
And this makes __contains__(in operator) a lot more efficient for sets than lists.
4. Sets can only contain hashtable item. If you try: set(([]1.[2])) you'll get a TypeError

Hashable:
An object is hashable if it has a hash value which never changes during its lifetime (it needs a __hash__() method),
and can be compared to other objects (it needs an __eq__() or __cmp__() method).
Hashable objects which compare equal must have the same hash value.

Hashability makes an object usable as a dictionary key and a set member,
because these data structures use the hash value internally.

All of Python’s immutable built-in objects are hashable, while no mutable containers (such as lists or dictionaries)
are. Objects which are instances of user-defined classes are hashable by default; they all compare unequal,
and their hash value is their id().
'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=list()
        brackets = {')':'(','}':'{',']':'['}
        for char in s:
            if char in brackets.values():
                stack.append(char)
            elif char in brackets.keys():
                 if len(stack) ==0 or stack.pop() != brackets[char]:
                    return False
            else:
                return False
        return stack==[]
solution = Solution()
teststr = "([)][][][][][()(]["
print ("The result of test result is " + str(solution.isValid(teststr)))

