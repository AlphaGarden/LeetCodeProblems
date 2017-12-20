'''
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
'''


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    return True
# First attempt : Try to use the binary search to solve the problem.
# Take care of the boundary problems.
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        if isBadVersion(start):
            return start
        if isBadVersion(end) and not isBadVersion(end-1):
            return end
        while(start <= end):
            mid = start + (end-start)/2

            if (isBadVersion(mid-1) and isBadVersion(mid+1)):
                end = mid - 1
            elif not isBadVersion(mid-1) and not isBadVersion(mid+1):
                start = mid + 1
            else:
                return mid if isBadVersion(mid) else mid+1
            # Attetion for ^^^^**** at the connection between ^ and * , the case of mid - 1 and mid + 1
            # will be the same, then we should take care of them.
