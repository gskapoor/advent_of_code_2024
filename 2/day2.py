def isLine(numStr):
    isDec = False
    if numStr[0] == numStr[1]:
        return False
    if numStr[0] < numStr[1]:
        isDec = True
    for i in range(len(numStr) - 1):
        if numStr[i] == numStr[i+1]:
            return False
        if isDec and numStr[i] > numStr[i + 1]:
            return False
        if (not isDec) and numStr[i] < numStr[i + 1]:
            return False
        difference = abs(numStr[i] - numStr[i + 1])
        if difference < 1 or difference > 3:
            return False
    return True

def part1(fileStr):
    lines = fileStr.split('\n')

    numSafe = 0
    for line in lines:
        if len(line) == 0:
            continue
        numStr = [int(num) for num in line.split()]
        if len(numStr) == 0:
            numSafe += 1
        elif isLine(numStr):
            numSafe += 1

    return numSafe

def part2(fileStr):
    lines = fileStr.split('\n')

    numSafe = 0
    for line in lines:
        if len(line) == 0:
            continue
        numStr = [int(num) for num in line.split()]
        if len(numStr) == 0:
            numSafe += 1
        elif isLine(numStr):
            numSafe += 1
        else:
            sublists = [numStr[:i] + numStr[i+1:] for i in range(len(numStr))]
            for sublist in sublists:
                if isLine(sublist):
                    numSafe += 1
                    break

    return numSafe

    return 0

filename = "input.txt"
file = open(filename, 'r')
content = file.read()
# content = "7 6 4 2 1\n1 2 7 8 9\n9 7 6 2 1\n1 3 2 4 5\n8 6 4 4 1\n1 3 6 7 9"

print(part1(content))
print(part2(content))

