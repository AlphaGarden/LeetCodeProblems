'''
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

Conclusion: Key point of the solution : we should know that the first thing to
solve a dynamic programming problem is to figure out the sub problem, and in this
question the sub problem is the
'''



class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Brute Force Method
        ans = nums[0]
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                ans = max(ans, sum(nums[i:j+1]))
        return ans
        # Optimized method
    # Dynamic programming
    def maxSubArray2(self,nums):
        dp = []
        dp.append(nums[0])
        ans = dp[0]
        for i in range(1,len(nums)):
            dp.append(nums[i] + (dp[i-1] if dp[i-1] >0 else 0))
            ans = max(ans,dp[i])
        return ans
solution = Solution()
testcase1 = [-2,1,2]
print solution.maxSubArray2(testcase1)