import utils.runner as runner

def solve(patternString):
    print(patternString)
    pattern = [int(i) for i in patternString]
    recipes = [3, 7]
    elve1 = 0
    elve2 = 1

    checkedUntil = 0

    while True:
        mate = recipes[elve1] + recipes[elve2]
        news = [int(r) for r in str(mate)]
        recipes += news
        elve1 = (elve1 + recipes[elve1] + 1) % len(recipes)
        elve2 = (elve2 + recipes[elve2] + 1) % len(recipes)

        while checkedUntil < len(recipes) - len(pattern):
            if recipes[checkedUntil:checkedUntil+len(pattern)] == pattern:
                print("")
                return checkedUntil
            checkedUntil += 1
            if checkedUntil % 1000 == 0:
                print(f"\r{checkedUntil}", end="")



if __name__ == "__main__":
    result = solve(runner.start().splitlines()[0])
    runner.done(result)
