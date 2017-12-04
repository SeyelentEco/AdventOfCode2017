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
        charfreq = dict()
        for char in word:
            if char in charfreq:
                charfreq[char] += 1
            else:
                charfreq[char] = 1
        wordlength = len(word)
        if wordlength in wordcount:
            #validate words
            for otherfreq in wordcount[wordlength]:
                #check if counts are the same
                wordsame = True
                for char, count in otherfreq.items():
                    if (char not in charfreq or charfreq[char] != count):
                        wordsame = False
                        break

                if (wordsame):
                    isvalid = False
                    break

            if (not isvalid):
                break
            wordcount[wordlength].append(charfreq)
        else:
            wordcount[wordlength] = [charfreq]
    print (input + " is " + ("True" if isvalid else "False"))
    if isvalid:
        isvalidcount += 1

    input = input_file.readline()

print(isvalidcount)
