"""
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
"""


# Solution Dynamic Programing
# For a house, we have two options rob or don't rob
# If we rob the current house, we are not able to rob the previous ajacent house
# If we don't rob the current house, we can rob the previous house.
# Then we can need to use d[i] to indicate the maximum money I can rob for the current house
"""
f(0) = nums[0]
f(1) = max(num[0], num[1])
f(k) = max( f(k-2) + nums[k], f(k-1) )
"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0 : return 0
        if len(nums) == 1 : return nums[0]
        memo = []
        memo.append(nums[0])
        memo.append(max(nums[0],nums[1]))
        for location in range(2, len(nums)):
            robbed = max((memo[location-2] + nums[location]),memo[location-1])
            memo.append(robbed)
        return memo[len(nums)-1]




if __name__ == '__main__':
    test_case = [1]
    solution = Solution()
    print solution.rob(test_case)