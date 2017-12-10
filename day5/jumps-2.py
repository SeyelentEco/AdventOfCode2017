input_file = open("input.txt", 'r')
instructions = input_file.readlines()
jumps = 0
idx = 0
print(instructions)
while idx < len(instructions):
    instruction = int(instructions[idx])
    instructions[idx] = instruction + (1 if instruction < 3 else -1)
    idx = idx + instruction
    jumps += 1
    #print(instructions)

print(jumps)
