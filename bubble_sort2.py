def bubble_sort(array:list):
    n = len(array)
    
    for i in range(n-1):
        for j in range(0, n-i-1):
            if array[j] > array[j+1] :
                array[j], array[j+1] = array[j+1], array[j]
 
array = [7,6,5,4,3,2,1]
 
bubble_sort(array)
print (array)

# Time complexity : O(n^2)
