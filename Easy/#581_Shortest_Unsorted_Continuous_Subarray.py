"""
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.
"""

"""
Solution attempt:
We can use the siliding window to solve the problem.
we should sort the original array A1 in the ascending order first, denoted as A2.
Then we should mark the beging and the end of the array as x and y.
If A1[x] is equal to the A2[x], then we add x by 1 util we meet the unequal one
If A2[y] is equal to the A2[y], then we minus y by 1 until we meet the unqual one.
Finally, we we get the smallest subarry
"""

import sys
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time complexity is O(nlogn) time and Space Complexity O(n)
        sorted_nums = sorted(nums)
        left, right = 0, len(nums) - 1
        while left != right:
            if (nums[left] != sorted_nums[left]) and (nums[right] != sorted_nums[right]):
                return right - left + 1
            elif nums[left] == sorted_nums[left]:
                left += 1
            elif nums[right] == sorted_nums[right]:
                right -= 1
        return 0
        # Time complexity is O(n) time and Space ComplexityO(1)
        # min_value, max_value = sys.maxint, -sys.maxint
        # flag = False
        # for i in range(1,len(nums)):
        #     if nums[i]<nums[i-1]:
        #         flag = True
        #     if flag:
        #         min_value = min(min_value,nums[i])
        # flag = False
        # for i in range(len(nums)-2,0,-1):
        #     if nums[i+1] < nums[i]:
        #         flag = True
        #     if flag:
        #         max_value = max(max_value,nums[i])
        # left, right = 0,0
        # for l in range(len(nums)):
        #     if min_value<nums[l]:
        #         left = l
        #         break
        # for r in range(len(nums)-1,0,-1):
        #     if max_value > nums[r]:
        #         right = r
        #         break
        # return 0 if right - left<0 else right- left + 1




if __name__ == '__main__':
    test_case = [2, 6, 4, 8, 10, 9, 15]
    solution = Solution()
    print (solution.findUnsortedSubarray(test_case))