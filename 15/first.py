import utils.runner as runner
from world import World

def solve(lines):
    world = World(lines)

    while world.round():
        pass

if __name__ == "__main__":
    result = solve(runner.start().splitlines())
    runner.done(result)
