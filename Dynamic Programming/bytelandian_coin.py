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

def exchange_mem(n, lookup):
  if lookup[n] == None:
    coins = exchange_mem(math.floor(n/2), lookup) + exchange_mem(math.floor(n/3), lookup) + exchange_mem(math.floor(n/4), lookup)
    if coins > n:
      lookup[n] = coins
    else:
      lookup[n] = n
  
  return lookup[n]



print("Enter the coin you want to exchange:")
n = int(input())
print(exchange_tabulate(n))
lookup = [None]*n+1
lookup[0] = 0
lookup[1] = 0
lookup[2] = 2
lookup[3] = 3
print(exchange_mem(n))
