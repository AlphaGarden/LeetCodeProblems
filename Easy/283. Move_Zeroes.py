'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.

'''

"""
we scan across the array and keep track of the position of zero
if we know get a non zero value, and we swap it with the zero position
At the same time we try to keep the correct position of zero
Finally we can remove the zero to the end
(Attention: we should know that the case that the value zero index which will not be equal to the index i when there are ajacent zero in the array )
"""
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero  = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                # the swapping element for python
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
solution = Solution()
sample_test = [0, 1, 0, 3, 12]
print (sample_test)