import utils.runner as runner
from base import Base

def solve(lines):
    base = Base(lines)
    return base.doors()

if __name__ == "__main__":
    result = solve(runner.start())
    runner.done(result)
