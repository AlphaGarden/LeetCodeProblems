# Given an integer , convert it to a roman numeral .
#
# Input is guaranteed to be within the range from 1 to 3999.
#
class Solution(object):
    def Digit0(self,num):
        return None
    def Digit1(self,num):
        return None
    def Digit2(self,num):
        return None
    def Digit3(self,num):
        return None
    def intToRoman(self, s):
        """
           :type s: str
           :rtype: int
           """
        result_str = ''
        if s == '0':
            return None
        for i in range(-1,-(len(s)+1),-1):
            if i == -1:
                return None




testnum='3999'
solution = Solution()
print solution.intToRoman(testnum)