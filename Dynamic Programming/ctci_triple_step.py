# Currently the max N value is 100.
def calc_steps(n, lookup):
  if(n < 0):
    return 0
  elif (n == 0):
    return 1
  else:
    if lookup[n] != None:
      return lookup[n]
    else:
      lookup[n] = calc_steps(n-1, lookup) + calc_steps(n-2, lookup) + calc_steps(n-3, lookup)
  return lookup[n]


print("Provide N(<100): ")
n = int(input())
lookup = [None] * 100
print("Total steps: ", calc_steps(n, lookup))
