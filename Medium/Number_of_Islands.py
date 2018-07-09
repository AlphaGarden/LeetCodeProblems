# coding=utf-8
'''

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or
vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3

Conclusoin:
For this problem.
If we want to know in which there is a '1' island symbol.
We need to iterate the entire matrix
Exploration_process
    If we get a '1' and the the indices are within the domain,
        cross it off as '0'
        then we continue to do the exploration process (up,down,left,right) to check
        whether there is a island symbol near the preceding one symbol
        until we  check joint island position, count it as 1 and return 1
    don't count and just return 0

Note:
Need to know the difference between DFS and BFS
Complexity analysis:
Time complexity: O(n^2)
'''
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def exploration(i,j):
            if 0<=i<len(grid) and 0<=j<len(grid[i]) and grid[i][j]=='1':
                #cross it off as 0
                grid[i][j]='0'
                map(exploration,(i,i,i+1,i-1),(j+1,j-1,j,j))
                return 1
            return 0
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                ans = ans+exploration(i,j)
        return ans
solution  = Solution()
geograph = [['1','0','0'],['0','1','0'],['0','1','1'],['0','0','0','1','0']]
print (solution.numIslands(geograph))