#  coding=utf-8
'''
Given n non-negative integers a1, a2, ..., an,
where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the most water.
Note: You may not slant the container and n is at least 2.

conclusion:
we define i as the beginning indices of the length, and j as the ending indices of the length
Besides we should know that the amount of water depends on the shorter bar.
Actually, we can use brute force method to solve the problem.
But the truth is that it will be out the time limit
And the we can think that we can think in this way:
If we want to find the max area from a list of data, we need to focus on the longest length at first.
If the length of ai is smaller than aj's
    we throw the bar ai away. then is i ++
    because we know that we still use ai and will never get potential max area
elif the length of ai is equal to aj,
    it doesn't matter for us to throw either ai or aj away.(i++,or j--)
    As I mentioned before, the max area depends on the shorter bar, then it means that it will
    be the same no matter which one we decide to throw away.
else:
    we throw the bar aj away. j--
    The reason is similar to the first one.

The reason why it works is because we always keep that in mind, we may get the max area if we
have the longest length, but we still go to explore those adjacent bar to check whether it
can construct a larger area.  And finally we get a larger area
 ^
 .
 7|
 6|
 5|       |
 4| |     |     |
 3| |     |     |  |
 2| |  |  |     |  |  |
 1|_| _| _| _| _| _| _|_>
 0 1  2  3  4  5  6  7...


'''


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height)-1
        max_ans = -1
        while (i<j):
            max_ans = max(max_ans,min(height[i],height[j])*(j-i))
            if height[i]<height[j]: i = i+1
            else: j = j-1
        return max_ans

a=[1,2,1]
solution = Solution()
print solution.maxArea(a)
