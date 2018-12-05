def forLetter(input):
    res = []
    for i in range(ord('a'), ord('z') + 1):
        print(chr(i).upper(), end="")
        letter = chr(i)
        line = input[:]
        line = line.replace(letter.lower(), "")
        line = line.replace(letter.upper(), "")
        r = solve(line)
        res.append(r)
        print(f" {r}")

    print("\nFound the minimum to be:")
    print(min(res))

def solve(line):
    startFrom = 0
    while True:
        found = False
        last = None

        for i in range(startFrom, len(line)):
            c = line[i]
            if (c.lower() == last and c.isupper()) or (c.upper() == last and c.islower()):
                newLine = line[:i-1] + line[i+1:]
                line = newLine
                startFrom = i - 2
                if startFrom < 0:
                    startFrom = 0
                found = True
                break

            last = c

        if not found:
            break
    return len(line)


with open("input.txt", "r") as file:
    forLetter(file.read().splitlines()[0])
