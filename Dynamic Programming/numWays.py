#Given a distance ‘dist, count total number of ways to cover the distance with 1, 2 and 3 steps.
#Link: https://www.geeksforgeeks.org/count-number-of-ways-to-cover-a-distance/

def countWays(dist, lookup):
  if dist < 0:
    return 0
  if not lookup[dist] == 0:
    return lookup[dist]
  
  lookup[dist] = countWays(dist-1, lookup) + countWays(dist-2, lookup) + countWays(dist-3, lookup)
  return lookup[dist]

dist = 4
lookup = [0] * (dist+1)
lookup[0] = 1
print(countWays(dist, lookup))
