letters = range(ord('a'),ord('z')+1)

def diff(ids):
    for i in range(0, len(ids)):
        for j in range(i, len(ids)):
            compare(ids[i], ids[j])

def compare(id1, id2):
    if id1 == id2:
        return
    for i in range(0, len(id1)):
        new1 = "".join([id1[j] for j in range(0, len(id1)) if j != i])
        new2 = "".join([id2[j] for j in range(0, len(id2)) if j != i])

        if new1 == new2:
            print("Found one!")
            print(new1)
            exit()


with open("input.txt") as file:
    diff(file.read().splitlines())
