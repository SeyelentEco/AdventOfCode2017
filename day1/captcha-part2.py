input_file = open("input.txt", 'r')

input = input_file.read()
input = input.strip(' \t\n\r')
same_sum = 0
idx = 0
chars = len(input)
print(input)
while idx < chars:
    current = int(input[idx])
    halfway = (chars/2 + idx) % chars
    halfwaynum = int(input[halfway])
    if (current == halfwaynum):
        same_sum += current
    idx += 1
print(same_sum)
