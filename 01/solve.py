def calcWith(lines):
    frequency = 0
    visited = []
    found = False
    num = 0

    while not found:
        for line in lines:
            frequency += int(line)

            if frequency in visited:
                print("The first frequency to be visited twice: %d" % frequency)
                break
                found = True
            else:
                visited.append(frequency)

            num += 1
            if num % 1000 == 0:
                print("Visited %d frequencies" % num)

    print("Final frequency: %d" % frequency)

with open("input.txt", "r") as inputFile:
    calcWith(inputFile.read().splitlines())
