def knapSack(W , wt , val , n): 
  
  dp = []
  for _ in wt:
    dp.append([0]*(W+1))
  max_ = 0
  for i in range(len(wt)):
    for j in range(1, W+1):
      if i == 0:
        if j >= wt[i]:
          dp[i][j] = val[i]
      elif j < wt[i]:
        dp[i][j] = dp[i-1][j]
      else:
        dp[i][j] = max(dp[i-1][j], val[i]+dp[i-1][j-wt[i]])
      max_ = max(max_, dp[i][j])
  for x in dp:
    print(x)
  return max_




# end of function knapSack 
  
# To test above function 
val = [1,4,5,7] 
wt = [1,3,4,5] 
W = 7
n = len(val) 
print (knapSack(W , wt , val , n) )
