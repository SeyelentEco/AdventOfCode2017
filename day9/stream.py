input_file = open("input.txt", 'r')
input = input_file.readline().strip()
#input = "{{{},{},{{}}}}"
depth = 0
sum = 0
ignore = False
ingarbage = False
index = -1
for char in input:
    index += 1
    print("Depth " +str(depth)+" Index "+str(index)+" ignore "+str(ignore)+" garbage "+str(ingarbage))

    if ignore:
        ignore = False
        continue
    if char == ">":
        ingarbage = False
        continue
    if char == "!":
        ignore = True
        continue
    if ingarbage:
        continue

    if char == "{":
        depth += 1
        sum += depth
    if char == "}":
        depth -= 1
    if char == "<":
        ingarbage = True

    #print("Depth " +str(depth)+" Index "+str(index))

    if (depth < 0):
        break

print("Sum: "+str(sum))
