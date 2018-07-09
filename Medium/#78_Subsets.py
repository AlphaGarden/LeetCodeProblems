"""

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

"""
# Back Tracking


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.backtrack([], res, nums, 0)
        return res

    def backtrack(self, path, res, nums, pos):
        res.append(path[:])
        while pos < len(nums):
            if nums[pos] in path : continue
            path.append(nums[pos])
            pos += 1
            self.backtrack(path, res, nums, pos)
            # Every time we finish the one function, we remove the lst element of the list
            path.pop(len(path)-1)


if __name__ == '__main__':
    solution = Solution()
    test_case = [1,2,3]
    print (solution.subsets(test_case))