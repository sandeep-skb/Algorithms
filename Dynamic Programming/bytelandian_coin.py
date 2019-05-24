'''
In Byteland they have a very strange monetary system.

Each Bytelandian gold coin has an integer number written on it. A coin n can be exchanged in a bank into three coins: n/2, n/3 and n/4. But these numbers are all rounded down (the banks have to make a profit).

You can also sell Bytelandian coins for American dollars. The exchange rate is 1:1. But you can not buy Bytelandian coins.

You have one gold coin. What is the maximum amount of American dollars you can get for it?
'''

import math
def exchange_tabulate(n):
  lookup = [0,0,2,3]
  
  for i in range(4,n+1):
    n2 = math.floor(i/2)
    n3 = math.floor(i/3)
    n4 = math.floor(i/4)
    if (n2 + n3 + n4) > i:
      lookup.append(n2+n3+n4)
    else:
      lookup.append(i)
  
  return lookup[n]


print("Enter the coin you want to exchange:")
n = int(input())
print(exchange_tabulate(n))
