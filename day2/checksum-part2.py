input_file = open("input.txt", 'r')
input = input_file.readline()
checksum = 0
while input:
    input = input.strip(' \t\n\r')
    numbers = input.split()
    idx = 0
    while (idx < len(numbers)):
        current = int(numbers[idx])
        idx2 = 0
        while (idx2 < len(numbers)):
            if (idx != idx2):
                test = int(numbers[idx2])
                if (current % test == 0):
                    checksum += (current/test)
                    break
            idx2 += 1
        idx += 1

    input = input_file.readline()

print(checksum)
