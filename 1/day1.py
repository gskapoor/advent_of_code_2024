

def part1(fileStr):
    lines = fileStr.split('\n')

    arr0 = []
    arr1 = []

    for line in lines:
        myInts = line.split('   ')
        if len(myInts) == 2:
            arr0.append(int(myInts[0]))
            arr1.append(int(myInts[1]))
    arr0.sort()
    arr1.sort()
    res = 0

    for i in range(len(arr0)):
        res += abs(arr0[i] - arr1[i])
    return res

def part2(fileStr):
    lines = fileStr.split('\n')

    arr0 = []
    arr1 = []

    for line in lines:
        myInts = line.split('   ')
        if len(myInts) == 2:
            arr0.append(int(myInts[0]))
            arr1.append(int(myInts[1]))
    myDict = {}
    for elem in arr1:
        if elem not in myDict:
            myDict[elem] = 0
        myDict[elem] += 1
    res = 0
    for elem in arr0:
        if elem in myDict:
            res += elem * myDict[elem]

    return res

filename = "input.txt"
file = open(filename, 'r')
content = file.read()

print(part1(content))
print(part2(content))

