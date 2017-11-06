# coding=utf-8
'''
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true

Conclusion:
For the pattern and the input:
As if we meet the '.' in the pattern:
The only thing we need to care about is whether or not the input still match when we remove
the . and character of text
As if we meet the '*' in the patern:
|----case1 : When the current value has 0 occurence before *, then we can ignore the current '*'
|            and preceding value to check if it still matches.
|            It means that the current value of text is not equal to '.' or the preceding value
|            of '*' but it still has chance to match.Think about it.
|
|
|----case2 : When the current value is eqaul to '.' the preceding value of '*', then we need
|            not only to check its match if we remove the '*' and its preceding value, but also
|            to take the situation when we remove the current value into consideration.
|            But both of them are the union relation.

'''


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        T = []
        len_s = len(s)
        len_p = len(p)
        for i in range(len_s+1):
            T.append([False for j in range(len_p+1)])
        T[0][0] = True
        for j in range(1,len_p+1,1):
            if p[j-1] == '*':
                T[0][j] = T[0][j - 2]
        for i in range(len_s):
            for j in range(len_p):
                if p[j] == '*':
                    T[i + 1][j + 1] = T[i + 1][j - 1]
                    if s[i] == p[j-1] or p[j-1] == '.':
                        T[i + 1][j + 1] = (T[i + 1][j + 1] or T[i][j + 1])
                elif p[j] == '.' or s[i] == p[j]:
                    T[i + 1][j + 1] = T[i][j]
                else:
                    T[i + 1][j + 1] = False
        print T
        return T[len_s][len_p]



solution = Solution()
pattern = "aba*"
text = "abb"
print solution.isMatch(text,pattern)
