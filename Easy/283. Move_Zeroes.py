'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.

'''


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero  = 0
        for i in xrange(len(nums)):
            if nums[i] != 0:
                # the swapping element for python
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
solution = Solution()
sample_test = [0, 1, 0, 3, 12]
print sample_test