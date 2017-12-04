import math

input = 265149

side = int(math.ceil(math.sqrt(input)))

if side % 2 == 0:
    side += 1

print("Creating a square with sides of : "+str(side))

startx = int(math.floor(side/2))
starty = startx
memory = [[0 for x in range(side)] for y in range(side)]
moves = []

move_idx = 0
cellx = startx
celly = cellx
memory[cellx][celly] = 1
# neighbor probes
probes = [[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1],[0,1],[1,1]]
neighborsum = 0
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

    neighborsum = 0
    for probe in probes:
        probex = cellx + probe[1]
        probey = celly + probe[0]
        if (probex >= 0 and probey >= 0 and probex < side and probey < side):
            neighborsum += memory[probex][probey]

    memory[cellx][celly] = neighborsum
    if (neighborsum > input):
        break
    move_idx += 1

print(neighborsum)
