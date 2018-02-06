"""
This is a demo for quick sort


If right > left
* Find the middle point to divide the array into two halves:
    * middle m = (l+r)/2
* Call mergeSort for first half:
    * Call mergeSort(array, left, m)
* Call mergeSort for second half:
    * Call mergeSort(array, m+1, right)
* Merge the two halves sorted in step2 and 3:
    * Call merge(array, left, m, right)


"""

class MergeSort:

    def go(self,array):
        if len(array) == 0 or len(array) == 1:
            return array
        else:
            self.sort(array, 0, len(array) - 1)

    def sort(self, array, left, right):
        if left < right:
            m = (left + right - 1)/2
            self.sort(array, left, m)
            self.sort(array, m+1, right)
            self.merge(array, left, m, right)

    def merge(self,array,left,m,right):
        # Create Temp array to store the sub array information
        left_T = array[left:m+1]  # from left to m
        right_T = array[m+1:right+1] # from m+1 to right

        # merge the two temp array into array[l:r]
        i = 0
        j = 0
        k = left
        while i<len(left_T) and j < len(right_T):
            if left_T[i] <= right_T[j]:
                array[k] = left_T[i]
                i += 1
            else:
                array[k] = right_T[i]
                j += 1
            k += 1

        # concatenate the number left in the left side
        while i<len(left_T):
            array[k] = left_T[i]
            k += 1
            i += 1
        # concatenate the number left in the right side
        while j<len(right_T):
            array[k] = right_T[j]
            k += 1
            j += 1


if __name__ == '__main__':
    solution = MergeSort()
    test_case = [2,4,5,2,2,4,5,9,7,1,3,2]
    solution.go(test_case)
    print test_case
