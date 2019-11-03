def mergeSort(arr):
  if len(arr) > 1:
    mid = len(arr)//2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    l = r = i = 0
    while(l < len(left) and r < len(right)):
      if left[l] < right[r]:
        arr[i] = left[l]
        l += 1
      else:
        arr[i] = right[r]
        r += 1
      i += 1
    
    arr[i:] = left[l:] + right[r:]
  
  return arr


arr = [60, 40, 50, 20, 10, 3, 80, 100]
print(mergeSort(arr))
