def InsertionSort(data):
    n = len(data)
    for i in range(n-1):
        key = data[i+1]
        j = i
        while j >= 0 and key < data[j]:
            data[j+1] = data[j]
            j -= 1
        data[j+1] = key
    return data

data = [9,8,1,4,2,7,5,10,6]
print(InsertionSort(data))
