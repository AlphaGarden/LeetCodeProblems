'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer

Example 1:

Input: 2
Output:  2
Explanation:  There are two ways to climb to the top.

1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output:  3
Explanation:  There are three ways to climb to the top.

1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Conclusion : the first thing we need to know is how to use the dynamic programing method to 
optimize this question and then try to find out the sub_problems.
In this case: the sub_problem is : we use dp[i] to describle how many ways we can use to climd to the Number i
Then we look at the dp[i-2] and dp[i-1] because we can use this two solved problems to sovle the dp[i],
because we can take 2 steps from dp[i-2] to dp[i] as well as 1 step from dp[i-1] to dp[i]
Then we could get the equation like : dp[i] = dp[i-1] + dp[i-2]
In the following two solutions:
The first one is Memorization method
The secod one is Bottom-up method
'''
class Solution(object):

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Trying to use dynamic programing
        # What if we define the sub_problems as Xi which is the number of way for us to climb to i
        # Memorizarion
        memo = [-1 for i in range(n + 1)]

        def iterate(num):
            # trivial case
            if num < 0:
                return 0
            elif num == 0:
                return 1
            elif memo[num] != -1:
                return memo[num]
            else:
                ans = iterate(num - 1) + iterate(num - 2)
                memo[num] = ans
                return ans
        iterate(n)
        return memo[n]

    # Bottom up method:
    def climbStairs2(self,n):
        dp = []
        dp.append(1)
        dp.append(1)
        for i in range(2, n+1):
            dp.append(dp[i-1] + dp[i-2])
        return dp[n]

solution = Solution()
testcases = [1, 2, 3, 4, 5, 6, 35]
for case in testcases:
    print (solution.climbStairs(case))
for case in testcases:
    print (solution.climbStairs2(case))