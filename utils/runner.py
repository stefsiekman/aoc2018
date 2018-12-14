import pyperclip
import sys

expectedResult = None

def start():
    """Return either de puzzle input or sample depending on the arguments."""
    global expectedResult

    # In case we're running an example
    if len(sys.argv) >= 2 and sys.argv[1].startswith("s"):
        with open("sample.txt", "r") as file:
            with open("result.txt", "r") as file2:
                expectedResult = file2.read().strip()
                return file.read().strip()

    # In case we're running the actual input
    else:
        # Try to read a file from argument
        filename = sys.argv[1] if len(sys.argv) >= 2 else "input.txt"
        with open(filename, "r") as file:
            return file.read()

def printLines(lines, padding=5):
    # Convert all lines to strings
    strings = [str(line) for line in lines]

    # Get the lengths and max length of all lines
    lengths = [len(s) for s in strings]
    maxLength = max(lengths)

    # Find the offset of each line
    offsets = [int((maxLength - length) / 2) for length in lengths]

    # Find the trailing padding of each line
    trails = [maxLength - l - o for l,o in zip(lengths, offsets)]

    # Print the header
    print(f"┏{'━'*padding}{'━'*maxLength}{'━'*padding}┓")

    # Print each line
    for i, (s, o, t) in enumerate(zip(strings, offsets, trails)):
        print(f"┃{' '*padding}{' '*o}{s}{' '*t}{' '*padding}┃")

        # Only print the separator on the not-last lines
        if i != len(strings) - 1:
            print(f"┠{'─'*padding}{'─'*maxLength}{'─'*padding}┨")

    # Print the footer
    print(f"┗{'━'*padding}{'━'*maxLength}{'━'*padding}┛")


def done(result):
    # If this was the actual result
    if expectedResult == None:
        pyperclip.copy(result)
        header = "Solution to the Puzzle"
        footer = "Copied to clipboard!"
        printLines([header, result, footer])

    # If this was the result to a sample
    else:
        lines = [
            "Sample Test Run".upper(),
            "Expected",
            expectedResult,
            "Actual",
            result,
            "TEST PASSED" if str(result).strip() == expectedResult else "TEST FAILED"
        ]
        printLines(lines)
