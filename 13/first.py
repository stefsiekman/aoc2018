import utils.runner as runner
from world import World

def solve(lines):
    world = World(lines)
    y,x = world.run()
    return f"{x},{y}"

if __name__ == "__main__":
    result = solve(runner.start().splitlines())
    runner.done(result)
