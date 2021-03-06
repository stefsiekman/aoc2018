import sys
from base import Base


def solve(regex):
    base = Base()
    base.parse(regex)

    print(f"There are {base.far_rooms()} at 1,000 or more doors away.")
    return 1


if __name__ == "__main__":
    filename = "input.txt" if len(sys.argv) < 2 else sys.argv[1]
    with open(filename, "r") as file:
        solve(file.read().strip())
