"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

"""

"""
The basic thought of the solution
Siliding Window:
We maintain a window with length p
"""
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        result = []
        hash_table = {}
        count = len(p)
        """
        Firstly, we construct a hash_table for each character in p
        """
        for c in p :
            if hash_table.has_key(c):
                hash_table[c] += 1
            else:
                hash_table[c] = 1
        print hash_table
        left = 0
        right = 0
        while right<len(s):
            """
            Each time if the character of s is in the hash_table, means that we get a possible character that we want,
            at the same time, we need to check whether this character is desirable or not based on its record in the hash_table
            And we only have the count minus 1 if the record in the hash_table is greater than 1 or equeal that 1, otherwise it 
            means that we already have enough this kind of character in the window. 
            """
            if hash_table.has_key(s[right]):
                if hash_table[s[right]] >= 1:
                    count -= 1
                hash_table[s[right]] -=1
            right += 1
            if count == 0 : result.append(left)
            if (right-left == len(p)):
                if hash_table.has_key(s[left]):
                    # If the value in the hash_table is <0, it means that the amount of character in the window is
                    # more than what we need, than we don't add 1 for the count
                    if hash_table[s[left]]>=0:
                        count += 1
                    hash_table[s[left]] += 1
                left += 1
        return result

if __name__ == '__main__':
    test_case_s = "cbaebabacd"
    test_case_p = "abc"
    solution = Solution()
    print solution.findAnagrams(test_case_s,test_case_p)