"""
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
Note:
The input string length won't exceed 1000.
"""


class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Solution based on Longest Palindromic Substring
        def expand_center(left, right):
            L = left
            R = right
            count = 0
            while 0 <= L and R < len(s) and s[L] == s[R]:
                L = L - 1
                R = R + 1
                count += 1
            return count

        ans = 0
        for i in range(len(s)):
            ans += (expand_center(i, i) + expand_center(i, i+1))
        return ans


if __name__ == '__main__':
    solution = Solution()
    test_case = "abc"
    print (solution.countSubstrings(test_case))
