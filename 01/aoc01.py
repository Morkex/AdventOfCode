file = "01\Input.txt"


def readFile(file):
    list = []
    f = open(file)
    for x in f:
        list.append(int(x))
    f.close()
    return list


def countIncrementsPart1(list):
    count = 0
    for i, actualDepth in enumerate(list):
        if i == 0:
            continue
        if actualDepth > list[i-1]:
            count += 1
    return count


def countIncrementsPart2(list):
    list3 = []
    for i, actualDepth in enumerate(list):
        actualDepth = list[i] + list[i+1] + list[i+2]
        list3.append(actualDepth)
        if i == len(list)-3:
            break
    return list3


print("Part1: " + str(countIncrementsPart1(readFile(file))))
print("Part2: " + str(countIncrementsPart1(countIncrementsPart2(readFile(file)))))
