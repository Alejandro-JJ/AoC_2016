from tools import GetInput, Text2Array, ReadTextInput
import numpy as np
GetInput(year=2016, day=1)

with open('./input_01.txt', 'r') as f:
    data = [(s[0], int(s[1:])) for s in f.read().strip().split(', ')]

dirs = [(-1,0), (0,1), (1,0), (0,-1)]  # rotating R
dir_idx = 0  # starting facing north
coord = (0,0) # starting point
visited = set(coord)

for turn, steps in data:
    if turn == 'R':
        dir_idx = (dir_idx + 1) % 4
    else:
        dir_idx = (dir_idx - 1) % 4
    move = dirs[dir_idx]
    
    for _ in range(steps):
        coord = (coord[0] + move[0], coord[1] + move[1])
        if coord in visited:
            print(f'Already visited {coord}!')
            break
        visited.add(coord)
    else:
        continue  # Only executed if the inner loop wasn't broken
    break  # Break the outer loop if a duplicate is found

print(f'Ended up {abs(coord[0]) + abs(coord[1])} blocks away.')

