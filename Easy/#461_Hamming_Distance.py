# coding=utf-8
'''
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

# The approach 
# First step, we convert the decimal number of x and y into binary number
# Secondly, we should pick up the number which has the shorter length.
# Thirdly, we compare the number with the corresponding number
# Then we figure out how many numbers of 1s are there in the number with longer length
# Rerturn the count

The above arrows point to positions where the corresponding bits are different.
'''


class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """

        # Approach 1: straight forward #
        # bx = bin(x)[2:]
        # by = bin(y)[2:]
        # i, count = -1, 0
        # long_s, short_s = '', ''
        # if len(bx) < len(by):
        #     short_s = bx
        #     long_s = by
        # else:
        #     long_s = bx
        #     short_s = by
        # while i >= -len(short_s):
        #     print short_s
        #     print long_s
        #     if short_s[i] != long_s[i]:
        #         count += 1
        #     i -= 1
        # for j in range(len(long_s)-len(short_s)):
        #     if long_s[j] == '1':
        #         count +=1
        # return count

        # Approach 2: one line code using the xor operator

        return bin(x^y).count('1')


solution = Solution()
t1 = 1
t2 = 4
print solution.hammingDistance(t1, t2)
