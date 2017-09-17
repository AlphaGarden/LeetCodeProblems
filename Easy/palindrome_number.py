# Assume that all negative numbers are not palindrome number
class Solution(object):
    def isPalindrome(self, x):
        if x > 0x7FFFFFFF or x< 0:
            return False
        num_str = str(x)
        num_len = len(num_str)
        if num_len == 1:
            return True
        else:
            j = -1
            for i in range(0, num_len / 2):
                if num_str[i] == num_str[j]:
                    j -= 1
                else:
                    return False
            return True
s = Solution()
testnum = -2147447412

print s.isPalindrome(testnum)
