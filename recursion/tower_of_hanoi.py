def tower_of_hanoi(n, src, dest, aux):
  if n == 1:
    print("Move disk {} from {} to {}".format(n, src, dest))
    return
  
  tower_of_hanoi(n-1, src, aux, dest)
  print("Move disk {} from {} to {}".format(n, src, dest))
  tower_of_hanoi(n-1, aux, dest, src)

print("Provide the number of disks: ")
n = int(input())
tower_of_hanoi(n, "A", "C", "B")
