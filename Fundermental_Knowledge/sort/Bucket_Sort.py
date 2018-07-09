import math


class BucketSort:
    def go(self,array):
        if len(array) == 0 or len(array) == 1:
            return array
        else:
            return self.sort(array, 3)

    def sort(self, array, b_size):
        # 1.Create n empty buckets
        min_value = min(array)
        max_value = max(array)
        bucket_count = int(math.floor((max_value - min_value) / b_size)) + 1
        bucket = [[] for i in range(bucket_count)]
        # 2.put array elements in different buckets
        for num in array:
            index = int(math.floor((num - min_value) / b_size))
            bucket[index].append(num)
        # 3.sort individual buckets
        for sub_bucket in bucket:
            sub_bucket.sort()
        # 4. concatenate all buckets into an array
        return self.reduce(lambda x, y: x + y, bucket)


if __name__ == '__main__':
    test_case = [2, 4, 5, 2, 2, 4, 5, 9, 7, 1, 3, 2]
    solution = BucketSort()
    print (solution.go(test_case))
