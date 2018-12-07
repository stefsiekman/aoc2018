import pyperclip

def solve(lines):
    return sum([int(i) for i in lines])

with open("input.txt", "r") as file:
    result = solve(file.read().splitlines())
    string = str(result)
    pyperclip.copy(result)
    resultLength = len(string)
    header = "Solution to the Puzzle"
    footer = "Copied to clipboard!"

    length = max(resultLength, len(header))

    resultOffset = int((length - resultLength) / 2)
    headerOffset = int((length - len(header)) / 2)
    footerOffset = int((length - len(footer)) / 2)

    resultTrail = length - resultLength - resultOffset
    headerTrail = length - len(header) - headerOffset
    footerTrail = length - len(footer) - footerOffset

    print("")
    print("")

    print(f"┏━━━━━{               '━'*length                }━━━━━┓")
    print(f"┃     {' '*headerOffset}{header}{' '*headerTrail}     ┃")
    print(f"┠─────{               '─'*length                }─────┨")
    print(f"┃     {' '*resultOffset}{result}{' '*resultTrail}     ┃")
    print(f"┠─────{               '─'*length                }─────┨")
    print(f"┃     {' '*footerOffset}{footer}{' '*footerTrail}     ┃")
    print(f"┗━━━━━{               '━'*length                }━━━━━┛")
