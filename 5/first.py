def solve(line):
    index = 0
    while index < len(line):
        found = False

        c = line[index]
        last = line[index-1] if index > 0 else None

        if (c.lower() == last and c.isupper()) or (c.upper() == last and c.islower()):
            newLine = line[:index-1] + line[index+1:]
            line = newLine
            index -= 2

        if len(line) % 1000 == 0:
            print(f"\r{len(line)}", end="")

        index += 1

    print(f"\r{len(line)}")


with open("input.txt", "r") as file:
    solve(file.read().splitlines()[0])
