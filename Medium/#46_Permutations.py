"""

"""

"""
Conclustion: One class of backtracking



"""

class Solution(object):
    # solution : backtracking
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.backtrack([],res,nums)
        return res
    def backtrack(self,path,res,nums):
        if len(path) == len(nums):
            res.append(path[:]) # save the copy of the list
        else:
            for i in nums:
                if i in path: continue
                path.append(i)
                self.backtrack(path,res,nums)
                path.remove(i)




if __name__ == '__main__':
    solution = Solution()
    test_case = [1, 2, 3]
    print solution.permute(test_case)
