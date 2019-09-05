#LCS Problem Statement: Given two sequences, find the length of longest subsequence present in both of them. 
#A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous.
#For example, “abc”, “abg”, “bdf”, “aeg”, ‘”acefg”, .. etc are subsequences of “abcdefg”.

def LCS(i, j, s1, s2, lookup):
  
  if i >= len(s1) or j >= len(s2):
    return 0
  print("i: ", i, "j: ", j, "s1: ", s1[i:], "s2: ", s2[j:])
  if not lookup[i][j] == -1:
    return lookup[i][j]
  if s1[i] == s2[j]:
    lookup[i][j] = 1 + LCS(i+1, j+1, s1, s2, lookup)
  else:
    lookup[i][j] = max(LCS(i+1, j, s1, s2, lookup), LCS(i, j+1, s1, s2, lookup))
  return lookup[i][j]


s1 = "AGGTAB"
s2 = "GXTXAYB"
lookup = []
for x in s1:
  lookup.append([-1]*len(s2))

print("Length of the longest common subsequence is: ", LCS(0, 0, s1, s2, lookup))
#for x in lookup:
#  print(x)
