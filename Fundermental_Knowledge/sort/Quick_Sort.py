"""
This is a demo for the quick sort
Pivot picking policy: pick the last one element as the pivot
"""


class QuickSort:
    def go(self, array):
        if len(array) == 0 or len(array) == 1:
            return array
        else:
            self.sort(array, 0, len(array) - 1)

    def sort(self, array, start, end):
       if start < end:
           # this pivot is already in the correct position
           pivot = self.partition(array, start, end)
           # sort the sub array from start to pivot - 1
           self.sort(array, start, pivot - 1)
           # sort the sub array form pivot to end
           self.sort(array, pivot + 1, end)

    def partition(self, array, low, high):
        """
        :param array: list[]
        :param low:Int 
        :param high: Int
        :return: Int
        This function takes last element as pivot, places
        the pivot element at its correct position in sorted
        array, and places all smaller (smaller than pivot)
        to left of pivot and all greater elements to right
        of pivot
        """
        # pick the last element as pivot
        pivot = array[high]
        # start to find out the right  position for pivot
        """
        we traverse the sub array from the beginning to the end with index j
            1. if array[j] is <= pivot, then we swap array[j] with the current number[i] greater than pivot
                (* Note that we actually label every current number greater than pivot with i*)
            2. else then just label this number because this number is a number[i] greater than pivot
        """
        i = low
        j = low
        while j <= high:
            if array[j] <= pivot:
                array[j], array[i] = array[i], array[j]
                # label the next greater number
                i += 1
            j += 1
        return i-1

if __name__ == '__main__':
    solution = QuickSort()
    test_case = [2, 4, 5, 2, 2, 4, 5, 9, 7, 1, 3, 2]
    partition_test_case = [10, 80, 30, 90, 40, 50, 70]
    solution.go(test_case)
    solution.partition(partition_test_case, 0, len(partition_test_case) - 1)
    print (partition_test_case)
    print (test_case)