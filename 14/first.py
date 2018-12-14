import utils.runner as runner

def solve(fromRecipe):
    recipes = [3, 7]
    elve1 = 0
    elve2 = 1

    while len(recipes) < fromRecipe + 10:
        mate = recipes[elve1] + recipes[elve2]
        news = [int(r) for r in str(mate)]
        recipes += news
        elve1 = (elve1 + recipes[elve1] + 1) % len(recipes)
        elve2 = (elve2 + recipes[elve2] + 1) % len(recipes)

    return "".join([str(r) for r in recipes[fromRecipe:fromRecipe+11]])

if __name__ == "__main__":
    result = solve(int(runner.start()))
    runner.done(result)
