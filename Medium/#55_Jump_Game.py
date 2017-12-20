'''

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:

A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.

Conclusion : Try to use the greedy algorithm to solve the problem.
'''


# Greedy Algorithm
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # first attempt: greedy algorithm
        max_edge = 0
        index = 0
        length = len(nums)
        while(index<length):
            max_edge = max(nums[index]+index, max_edge)
            if(max_edge >= length-1):
                return True
            elif(max_edge == index and nums[index]== 0):
                return False
            else:
                index += 1
        return False

solution = Solution()
testcases = [
    [2, 3, 1, 1, 4],
    [3, 2, 1, 0, 4]
]

for case in testcases:
    print solution.canJump(case)