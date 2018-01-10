class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        begin = 0
        length = len(nums)
        while(i<length):
            if nums[begin] == val:
                nums.remove(val)
                i += 1
                continue
            begin+=1
            i+=1
        return len(nums)


solution = Solution()
testcase1 = [3,3,3]
print solution.removeElement(testcase1,3)