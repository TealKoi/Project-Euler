#Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner

#How many such routes are there through a 20×20 grid?

import time

def find_paths(n):
  grid_size = n
  path_count = 0

  for i in range(0,grid_size+1):
    for j in range(i,grid_size+1):
      print(i,j)
      path_count += 1

  return path_count

def main():
  for i in range(1,5):
    print(find_paths(i))

if __name__ == "__main__":
  start_time = time.perf_counter()
  main()
  print("Program executed in {r:1.4f} second(s)".format(r=time.perf_counter()-start_time))