def binarySearch(arr, target):
  l = 0
  r = len(arr)-1
  while (l < r):
    mid = ((r-l)//2) + l
    if arr[mid] == target:
      return mid
    
    if arr[mid] < target:
      l = mid + 1
    else:
      r = mid
  if arr[l] == target:
    return l
  else:
    return -1

arr = [1,2,3,5,6]

# In the array
print(binarySearch(arr, 1))
print(binarySearch(arr, 2))
print(binarySearch(arr, 3))
print(binarySearch(arr, 5))
print(binarySearch(arr, 6))

#Not in the array
print(binarySearch(arr, 0))
print(binarySearch(arr, 4))
print(binarySearch(arr, 7))
