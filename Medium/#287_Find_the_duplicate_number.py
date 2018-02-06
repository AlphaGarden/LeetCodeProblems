"""
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive),
prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.

"""
"""
Solution : cycle detection

For each num[i] and index i , we define that the next value num[j] is at index num[i](j = num[i])
Assume that we have two points:
point 1 indicates a turtle which only take one step at a time
point 2 indicates a bunny which will take two step at a time
Additionally, for each num[i], we have 1<= num[i] <= n, 
therefore, we can guarantee that using num[i] as index will never go out of range
And, whenever we get to the situation that num[i] == num[j], we can say that we find a circle in this array
But at this time, we only get the intersection within the circle



"""


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ptr_i, ptr_j = 0, 0
        # To find the interaction
        while True:
            ptr_i = nums[ptr_i]
            ptr_j = nums[nums[ptr_j]]
            if nums[ptr_i] == nums[ptr_j]:
                break
        # To find the entrance
        # How to find ?
        ptr_i = nums[0]
        # Move to the intersection point
        ptr_j = nums[ptr_j]
        # Start to find the entrance of the loop
        while True:
            # As long as two points at the same position, they will have reach the entrance of the loop
            if ptr_i == ptr_j:
                return ptr_i
            ptr_i = nums[ptr_i]
            ptr_j = nums[ptr_j]


if __name__ == '__main__':

    solution = Solution()
    test_case = [2,5,9,6,9,3,8,9,7,1]
    print solution.findDuplicate(test_case)
