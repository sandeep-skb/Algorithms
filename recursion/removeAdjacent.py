#Recursively remove all adjacent duplicates
#https://www.geeksforgeeks.org/recursively-remove-adjacent-duplicates-given-string/

def removeAdjacent(chosen, remaining):
  if len(chosen) >= 2:
    if chosen[-1] == chosen[-2]:
      chosen = chosen[:-2]
  if len(remaining) == 0:
    return chosen
  ele = remaining[0]
  remaining = remaining[1:]
  chosen += ele
  return removeAdjacent(chosen, remaining)

print(removeAdjacent("", "ABCCBCBA"))
