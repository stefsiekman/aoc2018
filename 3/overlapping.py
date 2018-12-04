def overlapping(claims):
    claimeds = set()
    doubleds = set()
    doubles = 0

    total = len(claims)

    for claimIndex, claim in enumerate(claims):
        partsA = claim.split(" @ ")
        id = int(partsA[0][1:])

        partsB = partsA[1].split(": ")
        location = partsB[0].split(",")
        size = partsB[1].split("x")

        x = int(location[0])
        y = int(location[1])
        w = int(size[0])
        h = int(size[1])

        for i in range(x, x + w):
            for j in range(y, y + h):
                index = i + j * 20000

                claimed = index in claimeds
                doubled = claimed and index in doubleds

                if not claimed:
                    claimeds.add(index)
                elif not doubled:
                    doubleds.add(index)
                    doubles += 1

        done = claimIndex + 1
        percentage = round(done / total * 100)

        print(f"\rProcessed {percentage}%", end="")

    print("\nDone!")

    print(f"A total of {doubles} multi-claimed tiles were found")

with open("input.txt", "r") as file:
    overlapping(file.read().splitlines())
