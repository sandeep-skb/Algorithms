# Link: https://www.geeksforgeeks.org/partition-problem-dp-18/
# Partition problem is to determine whether a given set can be 
# partitioned into two subsets such that the sum of elements in both subsets is same

def DPpartition(arr, sum_):
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
  return dp[-1][-1] 



arr = [5,3,4,7] 
if not (sum(arr) % 2 == 0): 
  print("False")
else: 
  sum_ = sum(arr)//2
  print(DPpartition(arr, sum_))
