#input = "0  2   7   0"
input = "11	11	13	7	0	15	5	5	4	4	1	1	7	1	15	11"
banks = input.split()
print(banks)

iterations = 0

past = dict()

bankkey = ""
seenonce = False
while bankkey not in past:
    bankkey = ",".join(str(v) for v in banks)
    past[bankkey] = 1

    idx = 0
    maxbankidx = 0
    maxbank = 0
    while idx < len(banks):
        bank = int(banks[idx])
        if bank > maxbank:
            maxbankidx = idx
            maxbank = bank
        idx += 1

    # distribute
    banks[maxbankidx] = 0
    idx = maxbankidx + 1
    items = maxbank
    while items > 0:
        checkidx = idx % len(banks)
        bank = int(banks[checkidx])
        bank += 1
        banks[checkidx] = bank
        idx += 1
        items -= 1
    iterations += 1
    bankkey = ",".join(str(v) for v in banks)
    if bankkey in past and not seenonce:
        seenonce = True
        past = dict()
        iterations = 0
    print(banks)
print(iterations)
