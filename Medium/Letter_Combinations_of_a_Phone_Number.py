'''
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.

Conclusion:
The key part of solving this question is to know how to use reduce method of python
'''

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits=='': return []
        num_dicts = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        return (self.reduce(lambda x, y: [i + j for i in x for j in y], [num_dicts[i] for i in digits],['']))
solution = Solution()
input_string = "2"
print (solution.letterCombinations(input_string))