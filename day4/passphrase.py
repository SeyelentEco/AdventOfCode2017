import sys
input_file = open("input.txt", 'r')
input = input_file.readline()
isvalidcount = 0
while input:
    input = input.strip(' \t\n\r')
    words = input.split()
    wordcount = dict()
    isvalid = True
    for word in words:
        if word in wordcount:
            isvalid = False
            break

        wordcount[word] = 1

    if isvalid:
        isvalidcount += 1

    input = input_file.readline()

print(isvalidcount)
