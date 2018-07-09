"""
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k),
where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h.
Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.


Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
"""


"""
solution : 
Pick out tallest group of people and sort them in a subarray (S). 
Since there's no other groups of people taller than them, therefore each guy's index will be just as same as his k value.
For 2nd tallest group (and the rest), insert each one of them into (S) by k value. So on and so forth.
E.g.
input: [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
subarray after step 1: [[7,0], [7,1]]
subarray after step 2: [[7,0], [6,1], [7,1]]
"""
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []
        for p in sorted(people,key=lambda x:(-x[0],x[1])):
            """
            The key attribute in the sorted function,
            we can sort the list for multiple times by configuring the key parameter.
            Just like the above, firstly we sort the list by key[0](The height of people), then for each sub sorted list
            we sorted them by key[1](their k value)
            And finally we can get a sorted list for each subsection of the list
            """
            ans.insert(p[1], p)
        return ans


if __name__ == '__main__':
    solution = Solution()
    test_case = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
    print (solution.reconstructQueue(test_case))

    test_case2 = [[1,2,4],[1,2,1],[2,2,2],[1,1,1],[1,1,0]]
    print (sorted(test_case2,key=lambda x:(x[0],x[1],x[2])))