# we try to sort the heap in ascending order
class heapsort:

    
    def heapify(self, array, n, i):
        # we assume that lagrest value should be i
        largest = i
        # left child value
        l = 2 * i + 1
        # right child value
        r = 2 * i + 2
        
        # if the left child is greater than largest, set largest to be l
        if l < n and array[l] > array[largest]:
            largest = l

        
        # if the right child is greater than the current largest and set largest to be r
        if r < n and array[r] > array[largest]:
            largest = r

            
        # swap the root if needed
        if largest != i:
            array[i], array[largest] = array[largest], array[i]

            
            # At this time, we need to heapify the subtree of item which
            # is swapped with a smaller item, namely, largest index
            self.heapify(array, n, largest)

            
    def heapsort(self, arr):
        n = len(arr)

        
        # Build the max heap
        for i in range(n-1, -1, -1):
            self.heapify(arr, n, i )

            
        # Extract the max node to the heap and
        # put the max node to the current end of the array
        for i in range (n-1, 0, -1):
             arr[0],arr[i] = arr[i],arr[0]
             
             
             # after we remove the current max node of the heap, we need to
             # heapify the rest of the heap 
             self.heapify(arr, i, 0)

                
algorithm = heapsort()
test_case = [3, 5, 7, 2, 1, 6, 7, 0]
algorithm.heapsort(test_case)
for i in test_case:
    print(i)
