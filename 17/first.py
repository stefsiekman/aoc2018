import utils.runner as runner
from scan import Scan

def solve(lines):
    scan = Scan(lines)
    return scan.run()

if __name__ == "__main__":
    result = solve(runner.start().splitlines())
    runner.done(result)
