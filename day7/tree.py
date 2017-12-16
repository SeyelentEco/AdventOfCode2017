import re

input_file = open("input.txt", 'r')
commands = input_file.readlines()

commanddict = dict()

class Command:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.children = []
        self.parent = None
        self.childweight = 0

    def __str__(self):
        return "Name: "+self.name + " ("+str(self.weight)+") ("+str(self.childweight)+") Parent: "+(self.parent.name if self.parent is not None else "None")


for command in commands:
    matchObj = re.match( r'([a-z]+) \(([0-9]+)\)([ ->]*)([a-z, ]*)\n', command, re.M|re.I)

    name = (matchObj.group(1))
    weight = (matchObj.group(2))
    children = (matchObj.group(4).split(", "))
    #print(children)

    if name in commanddict:
        obj = commanddict[name]
        obj.weight = weight
    else:
        obj = Command(name, weight)
        commanddict[name] = obj

    for child in children:
        if (len(child) < 3):
            continue

        if child in commanddict:
            childobj = commanddict[child]
        else:
            childobj = Command(child, "0")
            commanddict[child] = childobj

        childobj.parent = obj
        obj.children.append(childobj)

#print(commanddict)
topcommand = None
for name, command in commanddict.items():
    #print(command)
    if command.parent is None:
        print(name)
        topcommand = command

def calculateChildWeight(command):
    childweight = 0
    weights = dict()
    for child in command.children:
        calculateChildWeight(child)
        childweight = childweight + int(child.childweight) + int(child.weight)
        key = str(int(child.weight) + child.childweight)
        if key in weights:
            weights[key].append(child)
        else:
            weights[key] = [child]
    if len(weights) > 1:
        print(weights)
        wrongnum = 0
        goodnum = 0
        for weight, children in weights.items():
            if len(children) == 1:
                wrongnum = int(weight)
            else:
                goodnum = int(weight)

        print("wrongnum: "+str(wrongnum))
        print("goodnum: "+str(goodnum))
        print("difference: "+str(wrongnum - goodnum))
        print(str(int(weights[str(wrongnum)][0].weight) - (wrongnum - goodnum)))

    command.childweight = childweight

calculateChildWeight(topcommand)
