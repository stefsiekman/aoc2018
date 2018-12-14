BOARD_SIZE = 1000

class Claim:

    def __init__(self, string):
        partsA = string.split(" @ ")
        self.id = int(partsA[0][1:])

        partsB = partsA[1].split(": ")
        location = partsB[0].split(",")
        size = partsB[1].split("x")

        self.x = int(location[0])
        self.y = int(location[1])
        self.w = int(size[0])
        self.h = int(size[1])

    def indices(self):
        return [x + y * BOARD_SIZE
                for x in range(self.x, self.x + self.w)
                for y in range(self.y, self.y + self.h)]

def claimList(claims):
    return

def overlapping(claimList):
    print("Allocating board memory space...")
    board = [0] * (BOARD_SIZE * BOARD_SIZE)
    claims = [Claim(c) for c in claimList]

    print("Stage A...")

    for claimIndex, claim in enumerate(claims):
        for index in claim.indices():
            if board[index] == 0:
                board[index] = claim.id
            else:
                board[index] = -1

    uniques = set()

    print("Stage B...")

    unqiueID = 0

    for claimIndex, claim in enumerate(claims):
        claimUnique = True
        for index in claim.indices():
            if board[index] != claim.id:
                claimUnique = False
                break
        if claimUnique:
            uniqueID = claim.id

    print(f"The unique claim is #{uniqueID}")

with open("input.txt", "r") as file:
    overlapping(file.read().splitlines())
