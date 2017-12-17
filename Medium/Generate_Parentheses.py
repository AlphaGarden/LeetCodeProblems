'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''

"""
        :type n: int
        :rtype: List[str]
        """
class Solution(object):
    def generateParenthesis(self, n):
        def generate(temp,left,right,parents=[]):
            if left: generate(temp+'(',left-1,right)
            if right> left: generate(temp + ')',left,right-1)
            if not right: parents.append(temp)
            return parents
        return generate('',n,n)



solution = Solution()
print solution.generateParenthesis(20)