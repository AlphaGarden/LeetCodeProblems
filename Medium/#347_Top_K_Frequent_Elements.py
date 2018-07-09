# coding=utf-8
"""
Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

"""

import math
class Solution(object):
    def bucketSort(self, table, b_size):
        # 1.Create n empty buckets
        min_value = min(table.values())
        max_value = max(table.values())
        bucket_count  = int(math.floor((max_value-min_value)/b_size)) + 1
        bucket = [[] for i in range(bucket_count)]
        # 2.put array elements in different buckets
        for i in table:
            index = int(math.floor((max_value - table[i])/b_size))
            bucket[index].append((i,table[i]))
        # 3.sort individual buckets
        for sub_bucket in bucket:
            sub_bucket.sort(key=lambda x: x[1], reverse= True)
        # 4. concatenate all buckets into an array
        return self.reduce(lambda x,y: x + y, bucket)

    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # hash_table = {}
        # # solution 1 Hash Table
        # # for counting the occurrence for each number, the time complexity is O(n)
        # for i in nums:
        #     if hash_table.has_key(i):
        #         hash_table[i] += 1
        #     else:
        #         hash_table[i] = 0
        # # for get the top k element, the time complexity is O(k)
        # return sorted(hash_table,key=hash_table.get)[-k:][::-1]

        # solution 2 Bucket Sort

        # 1.Construct the key:value hash_table for the array
        hash_table = {}
        ans = []
        for i in nums:
            if hash_table.has_key(i):
                hash_table[i] += 1
            else:
                hash_table[i] = 1
        # 2.Use bucket sort to get the top k frequecy index
        for record in self.bucketSort(hash_table, 2)[0:k]:
            ans.append(record[0])
        return ans

if __name__ == '__main__':
    test_case = [1,1,1,2,2,3,7,7,7,7,7,7,7]
    pick = 2
    solution = Solution()
    print (solution.topKFrequent(test_case,pick))

