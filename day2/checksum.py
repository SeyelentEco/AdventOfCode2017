import sys
input_file = open("input.txt", 'r')
input = input_file.readline()
checksum = 0
while input:
    input = input.strip(' \t\n\r')
    numbers = input.split()
    largest = -sys.maxsize
    smallest = sys.maxsize
    for num in numbers:
        num = int(num)
        if (num > largest):
            largest = num
        if (num < smallest):
            smallest = num

    checksum += largest - smallest

    input = input_file.readline()

print(checksum)
