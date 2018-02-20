"""

You are given a list of non-negative integers, a1, a2, ..., an, and a target, S.
Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3.
Output: 5
Explanation:

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.

"""
"""
Solution: Dynamic Programming
It is really similar to the knapsack problem
"""


class Solution(object):
    """
    Based on the observation of the brute force solution:
    we find out there is a lot redundant calculation among them,
    then we are going to use the memorization method to store the result for memo[i][sum]
    """

    def __init__(self):
        self.memo = {}

    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        return self.calculate(nums, 0, 0, S)

    # Sub-problem : The number of feasible combination for this node
    def calculate(self, nums, i, sums, S):
        if i == len(nums):
            return 1 if S == sums else 0
        else:
            if self.memo.has_key((i, sums)):
                return self.memo[(i, sums)]
            else:
                # if the current value of  (i, sums) are unknown, then we compute it
                # For the current node, we want to know how many combinations are there for
                # generate the target, and we are only necessary to thought from the bottom to
                # the top, as well as the add case and subtract case of that node respectively
                add = self.calculate(nums, i + 1, sums + nums[i], S)
                subtract = self.calculate(nums, i + 1, sums - nums[i], S)
                self.memo[(i, sums)] = add + subtract
        return self.memo[(i, sums)]

    # # Brute Force solution where the time complexity will be 2 power n
    # def __init__(self):
    #     self.count = 0
    #
    # def findTargetSumWays(self, nums, S):
    #     """
    #     :type nums: List[int]
    #     :type S: int
    #     :rtype: int
    #     """
    #     self.calculate(nums, 0, 0, S)
    #     return self.count
    #
    # def calculate(self, nums, i, sums, S):
    #     if i == len(nums):
    #         if sums == S:
    #             self.count += 1
    #     else:
    #         self.calculate(nums, i + 1, sums + nums[i], S)
    #         self.calculate(nums, i + 1, sums - nums[i], S)


if __name__ == '__main__':
    solution = Solution()
    test_case = [1, 1, 1, 1, 1]
    target = 3
    print(solution.findTargetSumWays(test_case, target))
