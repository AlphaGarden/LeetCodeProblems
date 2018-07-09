'''
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        window = set()
        length  = len(s)
        ans = 0
        i = 0
        j = 0
        while(i<length and j<length):
            if(s[j] not in window):
                window.add(s[j])
                j = j+1
                ans= max(ans,j-i)
            else:
                window.remove(s[i])
                i = i+1
        return ans

string = "ababababaabs"
solution = Solution()
print ("The length of longest substring of "+string+" is "+str(solution.lengthOfLongestSubstring(string)))