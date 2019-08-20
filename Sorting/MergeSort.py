def mergeSort(arr):
  if len(arr) > 1:
    middle = len(arr) // 2
    leftArr = arr[:middle]
    rightArr = arr[middle:]
    mergeSort(leftArr)
    mergeSort(rightArr)

    i = j = k = 0
    
    while(i < len(leftArr) and j < len(rightArr)):
      if leftArr[i] < rightArr[j]:
        arr[k] = leftArr[i]
        i += 1
      else:
        arr[k] = rightArr[j]
        j += 1
      k += 1
    
    while(i < len(leftArr)):
      arr[k] = leftArr[i]
      i += 1
      k += 1
    while(j < len(rightArr)):
      arr[k] = rightArr[j]
      j += 1
      k += 1
    print("left: ", leftArr, " right: ", rightArr, " --> ", arr, )
    

arr = [4,2,1,5,3,9]
leftStart = 0 
rightEnd = len(arr)
mergeSort(arr)
print("final: ", arr)
