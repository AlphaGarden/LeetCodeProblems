# coding=utf-8
'''
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Seen this question in a real interview before?
'''


class Solution(object):

    def singleNumber(self, nums):

        """
        :type nums: List[int]
        :rtype: int
        """
        # Approach 1 hash_table
        hash_table = {}
        for i in nums:
            try:
                hash_table.pop(i)
            except:
                hash_table[i] = 1
        return hash_table.popitem()[0]

    # Approach 2 math

    def singleNumber2(self,nums):
        return 2 * sum(set(nums)) - sum(nums)
    # Approach 3 Bit manipulation
    def singleNumber3(self,nums):
        ans = 0
        for i in nums:
            ans^=i
        return ans

    """
    If we take XOR of zero and some bit, it will return that bit
    a⊕0=a
    If we take XOR of two same bits, it will return 0
    a⊕a=0
    a⊕b⊕a=(a⊕a)⊕b=0⊕b=b
    """
