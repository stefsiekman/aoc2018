def forLetter(input):
    res = []
    for i in range(ord('a'), ord('z') + 1):
        print(chr(i))
        letter = chr(i)
        line = input[:]
        line = line.replace(letter.lower(), "")
        line = line.replace(letter.upper(), "")
        res.append(solve(line))

    print(min(res))

def solve(line):
    startFrom = 0
    prints = 0
    while True:
        found = False
        last = None

        for i in range(startFrom, len(line)):
            c = line[i]
            if (c.lower() == last and c.isupper()) or (c.upper() == last and c.islower()):
                newLine = line[:i-1] + line[i+1:]
                line = newLine
                startFrom = i - 10
                if startFrom < 0:
                    startFrom = 0
                found = True
                break

            last = c

        if len(line) % 1000 == 0:
            print(f"\r{len(line)}", end="")

        if not found:
            break
    print(f"\r{len(line)}")
    return len(line)


with open("input.txt", "r") as file:
    forLetter(file.read().splitlines()[0])
