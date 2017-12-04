import math

input = 265149
# if print memory is enabled, this script will allocate arrays to visualize what
# the memory looks like, don't enable for large numbers, it'll get slow
print_memory = False

# test input
if print_memory:
    input = 49

side = int(math.ceil(math.sqrt(input)))

if side % 2 == 0:
    side += 1

if print_memory:
    print("Creating a square with sides of : "+str(side))

startx = int(math.floor(side/2))
starty = startx
if print_memory:
    memory = [[0 for x in range(side)] for y in range(side)]
moves = []

move_idx = 0
cellx = startx
celly = cellx
if print_memory:
    memory[cellx][celly] = 1
for num in range(2, input+1):
    if (move_idx >= len(moves)):
        move_idx = 0
        current_side = int(math.ceil(math.sqrt(num)))
        if current_side % 2 == 0:
            current_side += 1

        moves = []
        moves.append([1, 0])
        moves += ([[0, -1] for x in range(current_side-2)])
        moves += ([[-1, 0] for x in range(current_side-1)])
        moves += ([[0, 1] for x in range(current_side-1)])
        moves += ([[1, 0] for x in range(current_side-1)])

    move = moves[move_idx]
    cellx += move[1]
    celly += move[0]

    if print_memory:
        memory[cellx][celly] = num

    move_idx += 1

distance = int(math.fabs(cellx - startx) + math.fabs(celly - starty))
print(distance)

if print_memory:
    print(memory)
