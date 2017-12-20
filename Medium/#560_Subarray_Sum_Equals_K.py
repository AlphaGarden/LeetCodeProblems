'''
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

Conclusion:
The key point is :
At the very beginning, we should maintain a hash table to store the occurance of sum[j], j from 0 to n-1

Because we should know the the equation: 
a[j] - a[i] = target.

In the other way. a[j] - target = a[i]

Then the only thing we need to do is to try to find out how many times of a[i],the sum, occurs in the preceding subarray.

And at anytime we get a sum[j] - target that occurs in the hash table, we should update the count variable with 
the number of times of the occurance of a[i]

'''
import collections
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Dynamic programming to solve this problem.
        # We should define the sub_problems.
        memo,num_sum,count = {0:1},0,0
        for i in nums:
            num_sum += i
            count += memo.get(num_sum - k,0)
            memo[num_sum] = memo.get(num_sum,0)+1
        return count

soluction = Solution()
print soluction.subarraySum([1,2,3,4,5],9)

