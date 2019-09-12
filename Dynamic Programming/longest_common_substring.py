# complexity o(NxM)
# Find the longest common substring length between two given strings.
def longest_common_substring(str1, str2):
  l1 = len(str1)
  l2 = len(str2)
  dp = []
  for _ in range(l2):
    dp.append([0]*l1)
  
  max_ = 0
  for i in range(l2):
    for j in range(l1):
      if str2[i] == str1[j]:
        if i-1 >= 0 and j-1 >= 0:
          dp[i][j] = 1 + dp[i-1][j-1]
        else:
          dp[i][j] = 1
        max_ = max(dp[i][j], max_)
  for x in dp:
    print(x)
  return max_

str1 = "abcdef"
str2 = "qbcdf"
if len(str2) > len(str1):
  str1, str2 = str2, str1

print(longest_common_substring(str1, str2))
