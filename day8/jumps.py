import sys

def valueCheck(value, test, testvalue):
    value = int(value)
    testvalue = int(testvalue)

    if test == "==":
        return value == testvalue
    elif test == ">":
        return value > testvalue
    elif test == ">=":
        return value >= testvalue
    elif test == "<":
        return value < testvalue
    elif test == "<=":
        return value <= testvalue
    elif test == "!=":
        return value != testvalue

    print("Error: unknown test: "+test)


input_file = open("input.txt", 'r')
input = input_file.readline()
registers = dict()
largestoverall = -sys.maxsize
while input:
    input = input.strip(' \t\n\r')
    instructions = input.split()
    print(instructions)
    if len(instructions) != 7:
        continue

    register = instructions[0]
    command = instructions[1]
    value = instructions[2]
    testregister = instructions[4]
    check = instructions[5]
    testvalue = instructions[6]

    currentvalue = registers[testregister] if testregister in registers else 0

    regvalue = registers[register] if register in registers else 0
    if valueCheck(currentvalue, check, testvalue):
        if command == "inc":
            registers[register] = regvalue + int(value)
        else:
            registers[register] = regvalue - int(value)
        
    if (register in registers and registers[register] > largestoverall):
        largestoverall = registers[register]

    input = input_file.readline()

print(registers)
largest = -sys.maxsize
largestregister = None
for register, value in registers.items():
    num = int(value)
    if (num > largest):
        largest = num
        largestregister = register

print(largest)
print(largestoverall)
