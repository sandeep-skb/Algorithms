# LINK: https://www.geeksforgeeks.org/longest-increasing-subsequence-dp-3/
# 
#Benchmarked recursion and DP implementation
# The Longest Increasing Subsequence (LIS) problem is to find the length of the longest subsequence of a given
# sequence such that all elements of the subsequence are sorted in increasing order. 
# For example, the length of LIS for {10, 22, 9, 33, 21, 50, 41, 60, 80} is 6 and LIS is {10, 22, 33, 50, 60, 80}.

import time
def LIS_recursion(chosen, remaining, count):
  if count < len(chosen):
    count = len(chosen)
  if not remaining:
    return count
  
  ele = remaining.pop(0)
  if not chosen:
    chosen.append(ele)
  elif chosen[-1] < ele:
    chosen.append(ele)
  count = LIS_recursion(chosen, remaining, count)
  if chosen:
    chosen.pop()
  count = LIS_recursion(chosen, remaining, count)
  remaining.insert(0, ele)
  return count

def LIS_dp(s1, count):
  dp = [1]*len(s1)
  for i in range(1, len(s1)):
    for j in range(0, i):
      if s1[i] > s1[j]:
        dp[i] = max(dp[i], (1+dp[j])) 
        count = max(count, dp[i])
  return count

s1 = [10, 22, 9, 33, 21, 50, 41, 60, 80]
#s1 = [3, 10, 2, 1, 20]
chosen = []
remaining = s1
count = 0
start = time.time()
print("length of the longest increasing subsequence in recurrsion way: ", LIS_recursion(chosen, remaining, count))
print("Time for recursion: {:.6f} sec ".format(time.time() - start))
count = 0
start = time.time()
print("length of the longest increasing subsequence in DP way: ", LIS_dp(s1, count))
print("Time for recursion: {:.6f} sec ".format(time.time() - start))
