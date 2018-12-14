import operator

class Guard:

    def __init__(self, id):
        self.id = id

        self.sleepTime = 0
        self.asleep = False
        self.working = False
        self.mins = [0] * 60

    def wakeUp(self, day, time):
        if not self.asleep:
            exit()

        self.asleep = False
        self.registerSleep(self.sinceTime, time)

    def sleep(self, day, time):
        self.asleep = True
        self.sinceTime = time

    def startShift(self):
        self.working = True
        self.asleep = False

    def endShift(self):
        if not self.working:
            exit()

        if self.asleep:
            exit()

        print(f"#{self.id} Ended")
        self.working = False

    def registerSleep(self, begin, end):
        self.sleepTime += end - begin
        for i in range(begin, end):
            self.mins[i] += 1

    def maxMin(self):
        mm = max(self.mins)

        for m in range(0, 60):
            if self.mins[m] == mm:
                return m

def solve(lines):

    currentGuard = None
    guards = {}

    for line in lines:
        partsA = line.split("] ")
        partsB = partsA[0].split(" 00:")
        day = partsB[0].split(" ")[0]
        print(line)

        if '#' in line:
            partsZ = line.split('#')
            partsY = partsZ[1].split(' ')
            newGuard = int(partsY[0])

            if currentGuard != None:
                currentGuard.endShift()

            # Create guard if required
            if not newGuard in guards:
                guards[newGuard] = Guard(newGuard)

            currentGuard = guards[newGuard]
            currentGuard.startShift()

        else:
            time = int(partsB[1])

            if partsA[1] == "wakes up":
                currentGuard.wakeUp(day, time)
            else:
                currentGuard.sleep(day, time)

    maxGuard = None
    for key in guards:
        guard = guards[key]
        if maxGuard == None:
            maxGuard = guard
            continue

        if max(guard.mins) > max(maxGuard.mins):
            maxGuard = guard

    print(f"Max guard {maxGuard.id}")
    print(f"Guard #{maxGuard.id} slept most, {maxGuard.mins[maxGuard.maxMin()]} at min {maxGuard.maxMin()}")
    print(f"Result = {maxGuard.id*maxGuard.maxMin()}")

with open("input.txt", "r") as file:
    solve(sorted(file.read().splitlines()))
