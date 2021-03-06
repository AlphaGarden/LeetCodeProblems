# coding=utf-8
'''
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime?

You may assume the returned list does not count as extra space.

Example:

Input:

[4,3,2,7,8,2,3,1]

Output:
[5,6]
'''


class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # python one line solver
        # return list(set(range(1,len(nums)+1)).difference(set(nums)))

        # fisrt we know that 1<= nums[i]<=n
        # then we can try to set the num[index] to be a negative num of its absolute num
        # and put it back to the num array
        # while the value in the array with negative value indicating that the index has occured
        # Fianlly, for those value with positive value, the index of that value will be the answer
        # Since there is no that index to modify the corresponding value to that index
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = -abs(nums[index])
        return [(i+1) for i in range(len(nums)) if nums[i] > 0]


solution = Solution()
test_sample = [4, 3, 2, 7, 8, 2, 3, 1]
print (solution.findDisappearedNumbers(test_sample))
