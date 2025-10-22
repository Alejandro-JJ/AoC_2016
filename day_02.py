from tools import *
GetInput(year=2016, day=2)

PAD = [[1,2,3], [4,5,6], [7,8,9]]
PAD_maxsize = 3
NEW_PAD = [[np.NaN, np.NaN, 1, np.NaN, np.NaN],
           [np.NaN, 2, 3, 4, np.NaN],
           [5, 6, 7, 8, 9],
           [np.NaN, 'A', 'B', 'C', np.NaN],
           [np.NaN, np.NaN, 'D', np.NaN, np.NaN]]
NEW_PAD_maxsize = 5

move_dic = {'U': (-1,0), 'D': (1,0), 'L': (0,-1), 'R': (0,1)}
with open('./input_02.txt', 'r') as f:
    instructions = [l for l in f.read().strip().split('\n')]

pos = (1,1)  # starting at '5'
sol = []
for line in instructions:
    for letter in line:
        move = move_dic[letter]
        potential_pos = (pos[0] + move[0], pos[1] + move[1])
        # Check that we do not move off the keypad
        if potential_pos[0] in range(NEW_PAD_maxsize) and potential_pos[1] in range(NEW_PAD_maxsize):
            # Check that the new position is not NaN
            if NEW_PAD[potential_pos[0]][potential_pos[1]] is not np.NaN:
                pos = potential_pos 
        else:
            pass
    # After a line has been read, we have a number to click
    new_number = NEW_PAD[pos[0]][pos[1]]
    sol.append(str(new_number))
print('Part 1 solution:', ''.join(sol))
    
        
        
    