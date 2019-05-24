'''
This has memoization, tabulation and recursion implementation along with the timer to tell the speed of each 
algo.
'''

import time
def fibo(n):
  if n == 0 or n==1:
    return 1
  else:
    return fibo(n-1)+fibo(n-2)

def fibo_memoize(n, lookup):
  if n == 0 or n==1:
    lookup[n] = 1
  if lookup[n] is None: 
    lookup[n] = fibo_memoize(n-1, lookup) + fibo_memoize(n-2, lookup)

  return lookup[n]

def fibo_tabulate(n, lookup):
  lookup[0] = 1
  lookup[1] = 1
  for i in range(2,n+1):
    lookup[i] = lookup[i-1] + lookup[i-2]
  
  return lookup[n]


def main():

  lookup = [None]*100
  start = time.time()
  print(fibo_memoize(40, lookup))
  end = time.time()
  print("timer of dp fibo: {0:.3f} ms".format((end - start)*1000))

  lookup = [None]*100
  start = time.time()
  print(fibo_tabulate(40, lookup))
  end = time.time()
  print("timer of dp fibo: {0:.3f} ms".format((end - start)*1000))

  start = time.time()
  print(fibo(40))
  end = time.time()
  print("timer of regular: {} secs".format(end - start))

if __name__ == "__main__":
  main()
