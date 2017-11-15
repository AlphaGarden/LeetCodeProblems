'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
Conclusion:
The key steps:
1.Try to sort the list firstly. Because it will reduce the time of iterating
2.Then in terms of the iterating pattern, we should pick each number as an answer,
and then go search search the following potential pair such that the sum is zero.
3.The last thing is to take care of the duplicated answer, we only care about the number we meet
at the first time, then skip those duplicated numbers
'''
class Solution(object):
    def threeSum(self, nums):
        sort_nums = sorted(nums)
        ans = []
        for i in range(len(nums)-2):
            # Use the first number of those duplicated sequence
            if i>0 and sort_nums[i]==sort_nums[i-1]:
                continue
            left,right = i+1,len(nums)-1
            while left < right:
                s = sort_nums[i] + sort_nums[left] + sort_nums[right]
                # Skip duplicated sequence
                while sort_nums[left] == sort_nums[left + 1]:
                    left = left + 1
                while sort_nums[right] == sort_nums[right - 1]:
                    right = right - 1
                # we increase the left(min) value
                if s < 0 :
                    left = left + 1
                # we decrease the right(max) value
                elif s > 0 :
                    right = right -1
                # we get the pair such that the sum are zero
                else:
                    ans.append([sort_nums[i],sort_nums[left],sort_nums[right]])
                    left = left + 1
                    right = right -1
        return ans
S = [-4, -1, -1,-1, 0, 1, 2]
solution = Solution()

print solution.threeSum(S)



'''
        list_len = len(nums)
        if list_len<3: return []
        pair_i = 0
        pair_j = 1
        ans = []
        while(pair_j < list_len-1):
            pair_sum = nums[pair_i]+nums[pair_j]
            for walker in range(pair_j+1,list_len,1):
                print walker
                if pair_sum + nums[walker] == 0: ans.append([nums[pair_i],nums[pair_j],nums[walker]])
            pair_i = pair_i + 1
            pair_j = pair_j + 1
'''