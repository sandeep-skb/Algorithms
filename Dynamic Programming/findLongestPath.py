# LINK: https://www.geeksforgeeks.org/find-the-longest-path-in-a-matrix-with-given-constraints/
# Given a n*n matrix where all numbers are distinct, find the maximum length path (starting from any cell) such that 
# all cells along the path are in increasing order with a difference of 1. We can move in 4 directions from a given 
# cell (i, j), i.e., we can move to (i+1, j) or (i, j+1) or (i-1, j) or (i, j-1) with the 
# condition that the adjacent cells have a difference of 1.


def findLongest(mat, i, j, dp, cur, max_):
  if (i < 0 or i >= len(mat)) or (j < 0 or  j >= len(mat[0])):
    return max_
  dp[i][j] = cur
  if cur > max_:
    max_ = cur
  
  if (i-1 >= 0) and (mat[i-1][j] == (mat[i][j] + 1)):
    max_ = findLongest(mat, i-1, j, dp, cur+1, max_)
  
  if (i+1 < len(mat)) and (mat[i+1][j] == (mat[i][j] + 1)):
    max_ = findLongest(mat, i+1, j, dp, cur+1, max_)
  
  if (j-1 >= 0) and (mat[i][j-1] == (mat[i][j] + 1)):
    max_ = findLongest(mat, i, j-1, dp, cur+1, max_)
  
  if (j+1 < len(mat[0])) and (mat[i][j+1] == (mat[i][j] + 1)):
    max_ = findLongest(mat, i, j+1, dp, cur+1, max_)
  
  return max_




mat = [[ 1, 2, 9 ], 
       [ 5, 3, 8 ], 
       [ 4, 6, 7 ]]
max_ = 0
dp = []
for _ in mat:
  dp.append([0] * len(mat[0]))

for i in range(len(mat)):
  for j in range(len(mat[0])):
    if dp[i][j] == 0:
      cur = 0
      max_ = findLongest(mat, i, j, dp, cur+1, max_)

for x in dp:
  print(x)

print(max_)
