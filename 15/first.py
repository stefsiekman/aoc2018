import utils.runner as runner
from world import World

def solve(lines):
    world = World(lines)

    round = 1
    while world.round():
        round += 1
        pass

    return world.outcome()

if __name__ == "__main__":
    result = solve(runner.start().splitlines())
    runner.done(result)
