#insert
#delete
#replace
def editDistance(str1, str2, m , n, lookup):
  if m == 0:
    lookup[m][n] = n
    return n
  if n == 0:
    lookup[m][n] = m
    return m

  if not lookup[m-1][n-1] == -1:
    return lookup[m-1][n-1]

  if str1[m-1] == str2[n-1]:
    lookup[m-1][n-1] = editDistance(str1, str2, m-1, n-1, lookup)
  else:
    lookup[m-1][n-1] = 1 + min(editDistance(str1, str2, m-1, n, lookup), editDistance(str1, str2, m, n-1, lookup), editDistance(str1, str2, m-1, n-1, lookup))
  return lookup[m-1][n-1]

lookup = []
str1 = "sunday"
str2 = "saturday"
for _ in str1:
  lookup.append([-1]*len(str2))
res = editDistance(str1, str2, len(str1), len(str2), lookup)
for x in lookup:
  print(x)

print("ans: ", res)
