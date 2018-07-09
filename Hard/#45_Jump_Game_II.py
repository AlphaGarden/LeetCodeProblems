'''

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

Note:
You can assume that you can always reach the last index.

Conclusion:
1.The key point to solve this problem is to solve the problem by greedy algorithm.
2.we can try to keep track of the farthest postion we could go while iterate through the array.
3.Then the most tricky part is that we can think that we are able to jump to the farthest position whenever we reach 
the current end position of the array.
4.
'''


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Attetion that you should know the presume is that we have assume that we can always reach the last
        # index for any array.
        index,max_edge,cur_end, count = 0, 0, 0, 0
        length = len(nums)
        while index < length-1: # we are not going to check the end of the array since we are not necessary to check.
            max_edge = max(max_edge, index + nums[index]) # the farthest position we can go before we reach the current end
            if index == cur_end:
                # when we reach the current end of the array we say that add the count to imply that
                # we pick the jump which can lead us to the farthest place so that we plus the jump
                count += 1
                cur_end = max_edge # Then we jump the current end to the farthest position.
                if max_edge > length-1:
                    return count
            index += 1
        return count

# test case
solution = Solution()
test_case = [
    [2, 3, 1, 1, 4],
    [1, 1, 1, 1, 1],
    [4, 2, 0, 3, 0, 1, 1],
    [1,2,3,4,5]
]

for case in test_case:
    print (solution.jump(case))