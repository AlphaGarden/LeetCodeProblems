# coding=utf-8
"""

Given an array of size n, find the majority element.

The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Credits:

Special thanks to @ts for adding this problem and creating all test cases.

"""
import collections

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time Limit Exceeded
        # for i in nums:
        #     if nums.count(i) > len(nums)/2:
        #         return i

        # with hash map
        # The most important part of this method is to use the hash map to keep the record of how many
        # the number is in the list
        record = {}
        for i in nums:
            try:
                record[i] += record[i] + 1

            except:
                record[i] = 1
        return max(record, key = record.get)



solution = Solution()

array = [1,2,3,4,4,4,4,4]

print solution.majorityElement(array)
