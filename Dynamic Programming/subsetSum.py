#Link: https://www.geeksforgeeks.org/subset-sum-problem-dp-25/
#Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum.
#Solved in recursion and DP way.
def isSubsetSum(set_, n, sum_):
  #print("isSubsetSum(", n , "set: ", set_[n]" ,", sum_ ," )" )
  if n < 0:
    return False
  if sum_ < 0:
    return False
  if sum_ == 0:
    return True
  
  return (isSubsetSum(set_, n-1, sum_) or isSubsetSum(set_, n-1, (sum_ - set_[n-1])))

def dpIsSubsetSum(set_, n, sum_):
  dp = []
  for _ in range(n):
    dp.append([False] * (sum_+1))

  #Setting the ground Truth
  for i in range(n):
    dp[i][0] = True

  for i in range(n):
    for j in range(sum_+1):
      if i == 0:
        if set_[i] == j:
          dp[i][j] = True
        continue
      if set_[i] > j:
        dp[i][j] = dp[i-1][j]
      else:
        dp[i][j] = dp[i-1][j] or dp[i-1][j-set_[i]]
  return dp  


set_ = [3, 34, 4, 12, 5, 2] 
#set_ = [2,3,7,8,10]
sum_ = 10
n = len(set_)
if isSubsetSum(set_, n, sum_):
  print("Recursion: There is a subset")
else:
  print("Recursion: There is no subset")

dp = dpIsSubsetSum(set_, n, sum_)

if dp[-1][-1]:
  print("DP: There is a subset")
else:
  print("DP: There is no subset")
