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


class Solution(object):
    def generateParenthesis(self, n):
        def generate(temp,left,right,parents=[]):
            if left: generate(temp+'(',left-1,right)
            if right> left:
        """
        :type n: int
        :rtype: List[str]
        """

solution = Solution()
print solution.generateParenthesis(4)