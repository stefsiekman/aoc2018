letters = range(ord('a'),ord('z')+1)
def checksum(ids):
    twos = 0
    threes = 0

    for id in ids:
        # See if there are two of any character
        for l in letters:
            if id.count(chr(l)) == 2:
                twos += 1
                break
        for l in letters:
            if id.count(chr(l)) == 3:
                threes += 1
                break

    print(f"{twos} {threes}")
    return twos * threes


with open("input.txt") as file:
    print(checksum(file.read().splitlines()))
