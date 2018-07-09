"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.
"""

import sys
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ans = 0
        min_buy  = sys.maxint
        for i in prices:
            if i < min_buy:
                min_buy = i
            elif (i - min_buy) > ans:
                ans = i - min_buy
        return ans



if __name__ == '__main__':
    test_case = [7, 6, 4, 3, 1]
    test_case_2 = [7, 1, 5, 3, 6, 4]
    solution = Solution()
    print (solution.maxProfit(test_case_2))