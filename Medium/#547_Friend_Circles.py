"""
DiscussPick One
There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

Example 1:
Input:
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle.
The 2nd student himself is in a friend circle. So return 2.
Example 2:
Input:
[[1,1,0],
 [1,1,1],
 [0,1,1]]
Output: 1
Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends,
so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.
Note:
N is in range [1,200].
M[i][i] = 1 for all students.
If M[i][j] = 1, then M[j][i] = 1.
"""


"""
Conclusion:
The basic idea is to use dfs to check every node whether it is visited or not.
If it is not visted, we try to use this node to check the others out,
and see if we can find the others node, and update that node as visited.

Finally, after the exploration, we will find the circle.

And then we loop the visited list to check out whether there is unvisited person left or not.
If so back to exploration process.
"""

class Solution(object):
    def dfs(self, person, M, visited):
        for other in range(len(M)):
            if M[person][other] == 1 and not visited[other]:
                visited[other] = True
                self.dfs(other, M, visited)
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        visted = [False for i in range(len(M))]
        count = 0
        for person in range(len(M)):
            if not visted[person]:
                self.dfs(person, M, visted)
                count += 1
        return count


if __name__ == '__main__':
    test_case_1 = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    test_case_2 = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
    test_case_3 = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
    solution = Solution()
    print solution.findCircleNum(test_case_1)
    print solution.findCircleNum(test_case_2)
    print solution.findCircleNum(test_case_3)



