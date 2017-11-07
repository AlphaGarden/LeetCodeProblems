# coding=utf-8
'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
Example:

Input: "cbbd"

Output: "bb"

Conclusion:
Because the time complexity is O(n^3) and it doesn't work

The another method is to use the basic idea
Well:
As we know, If the string is palindromic.
We could find a center.
For example "aba", then the center is 'b'
but the center also could be the place between two character
For example "aa", then the center is between 'aa'
Totally, we have 2n - 1 centers
Here is the strategy we do:
        we check the every center and expand the string to get the possible palindrome and compare their length
And finally we can get the longest length.
And the time complexity is O(n^2)
And the space complexity is O(1)

'''


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        #
        #  Brute Force method

        # ans = ''
        # def is_palindrome(str):
        #     return str == str[::-1]
        # for i in range(len(s)):
        #     for j in range(len(s),0,-1):
        #         if is_palindrome(s[i:j]) and  j-i >= len(ans):
        #             ans = s[i:j]
        # return ans

        # Expand Palindrome center
        def expand_center(left,right):
            L = left
            R = right
            while 0<= L and R <len(s) and s[L]==s[R]:
                L = L - 1
                R = R + 1
            return R - L - 1

        start = 0
        end = 0
        for i in range(len(s)):
            len1 = expand_center(i,i)
            len2 = expand_center(i,i+1)
            m_len = max(len1,len2)
            if m_len > (end - start):
                start = i - (m_len)/2
                end = i + m_len/2
        return s[start:end+1]

solution = Solution()
test_str = 'abbabba'
test_str2="flsuqzhtcahnyickkgtfnlyzwjuiwqiexthpzvcweqzeqpmqwkydhsfipcdrsjkefehhesubkirhalgnevjug" \
          "fohwnlhbjfewiunlgmomxkafuuokesvfmcnvseixkkzekuinmcbmttzgsqeqbrtlwyqgiquyylaswlgfflr" \
          "ezaxtjobltcnpjsaslyviviosxorjsfncqirsjpkgajkfpoxxmvsyynbbovieoothpjgncfwcvpkvjcmrcuor" \
          "onrfjcppbisqbzkgpnycqljpjlgeciaqrnqyxzedzkqpqsszovkgtcgxqgkflpmrikksaupukdvkzbltvefitdeg" \
          "nlmzeirotrfeaueqpzppnsjpspgomyezrlxsqlfcjrkglyvzvqakhtvfmeootbtbwfhqucbnuwznigoyatvkocqmbtq" \
          "ghybwrhmyvvuchjpvjckiryvjfxabezchynfxnpqaeampvaapgmvoylyutymdhvhqfmrlmzkhuhupizqiujpwzarnszrexpvg" \
          "dmtoxvjygjpmiadzdcxtggwamkbwrkeplesupagievwsaaletcuxtpsxmbmeztcylsjxvhzrqizdmgjfyftpzpgxateopwvy" \
          "nljzffszkzzqgofdlwyknqfruhdkvmvrrjpijcjomnrjjubfccaypkpfokohvkqndptciqqiscvmpozlyyrwobeuazsaw" \
          "timnawquogrohcrnmexiwvjxgwhmtpykqlcfacuadyhaotmmxevqwarppknoxthsmrrknu"
print len(test_str2)
print solution.longestPalindrome(test_str)