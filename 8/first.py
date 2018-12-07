import pyperclip
import utils.runner as runner

def solve(lines):
    print("Solving the puzzle...")
    return sum([int(line) for line in lines])

if __name__ == "__main__":
    result = solve(runner.start().splitlines())
    runner.done(result)
