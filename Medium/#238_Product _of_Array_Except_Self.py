"""
Given an array of n integers where n > 1, nums,
return an array output such that output[i] is equalto the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)
"""

# Solution left to me and right to me
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = 1
        n = len(nums)
        output = []
        # we use the output to stash the left product except nums[i]
        for i in range(n):
            output.append(left)
            left = left * nums[i]
        right = 1
        # we every time update the output everytime we get the right profuct expcept nums[i]
        for i in range(n-1,-1,-1):
            output[i] = right * output[i]
            right = right* nums[i]
        return output

if __name__ == '__main__':
    solution = Solution()
    test_case = [1, 2, 3, 4]
    print solution.productExceptSelf(test_case)
