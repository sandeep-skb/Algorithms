#https://www.geeksforgeeks.org/partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum/
#Partition a set into two subsets such that the difference of subset sums is minimum

# Idea here is the create a dp table [len(arr)]x[sum//2 + 1].
# Whatever is the closest value to sum//2 + 1 we get that is sum of one set. subtract that for the other subset to get
# the minimum distance.

def DPfindMin(arr, sum_):
  orig_sum = sum_
  sum_ = (sum_ // 2) + 1
  dp = []
  for _ in range(len(arr)):
    dp.append([False] * (sum_+1))

  for i in range(len(arr)):
    dp[i][0] = True
  
  for j in range(sum_+1):
    if arr[0] == j:
      dp[0][j] = True
      break

  for i in range(len(arr)):
    for j in range(sum_+1):
      if arr[i] > j:
        dp[i][j] = dp[i-1][j]
      else:
        dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i]]
  
  for j in range(sum_, -1, -1):
    if dp[-1][j] == True:
      return abs(orig_sum - j - j)



arr = [11,11,0] 

sum_ = sum(arr)
print(DPfindMin(arr, sum_))
