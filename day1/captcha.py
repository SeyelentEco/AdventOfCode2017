input_file = open("input.txt", 'r')

input = input_file.read()
input = input.strip(' \t\n\r')

last_char = ''
same_sum = 0
same_chars = []
for char in input:
    if last_char == char:
        same_sum += int(char)
        same_chars.append(char)
    last_char = char

if len(input) > 0 and input[0] == input[-1]:
    same_sum += int(input[0])
    same_chars.append(char)

print(same_sum)
