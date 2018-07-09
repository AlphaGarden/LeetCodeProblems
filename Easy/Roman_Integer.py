# Given a roman numeral, convert it to an integer.
#
# Input is guaranteed to be within the range from 1 to 3999.
#
class Solution(object):
    def value(self,r):
        if (r == 'I'):
            return 1
        if (r == 'V'):
            return 5
        if (r == 'X'):
            return 10
        if (r == 'L'):
            return 50
        if (r == 'C'):
            return 100
        if (r == 'D'):
            return 500
        if (r == 'M'):
            return 1000
        return -1
    def romanToInt(self, s):
        # This function returns value of each Roman symbol
        i = 0
        result = 0
        while(i<len(s)):
            s1 = self.value(s[i])
            if(i+1<len(s)):
                s2 = self.value(s[i+1])
                if(s1>=s2):
                    result = result+s1
                    i = i+1
                else:
                    result = result+s2-s1
                    i = i+2
            else:
                result = result+s1
                return result
        return result

testnum="MCMXCVI"
solution = Solution()
print (solution.romanToInt(testnum))