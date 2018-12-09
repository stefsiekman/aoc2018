tasksTotal = 100
tasksDone = None
tasksStep = 1
barWidth = 80
totalWidth = 80

def setup(tasks, width=80):
    global tasksTotal, tasksStep, barWidth, totalWidth
    tasksTotal = tasks
    tasksStep = int(tasks / 1000)
    totalWidth = width
    barWidth = totalWidth - 5 - 6

def calcLabelPadding(label, space):
    labelLength = len(str(label))
    left = int((space - labelLength) / 2)
    right = space - labelLength - left
    return (left, right)

def labeledSide(label, length, char):
    labelLength = len(str(label))
    if labelLength < length - 4:
        line = ""
        padding = calcLabelPadding(label, length)
        line += char * (padding[0] - 1)
        line += f" {str(label)} "
        line += char * (padding[1] - 1)
        return line
    else:
        return char * length

def done(done):
    global tasksDone

    # Check if it's time for a print (at every 0.1%)
    if done % tasksStep != 0:
        return

    tasksDone = done
    line = '\r'

    # Done section
    doneLength = round(tasksDone/tasksTotal * barWidth)
    line += labeledSide(tasksDone, doneLength, '█')

    # Todo section
    todoLength = barWidth - doneLength
    line += labeledSide(tasksTotal, todoLength, '━')
    line += '' * todoLength

    # Percentage
    percentageString = str(round(tasksDone/tasksTotal * 100))
    percentagePadding = 3 - len(percentageString)
    line += ' ' + ' ' * percentagePadding
    line += percentageString
    line += '%'

    # Print the line
    print(line, end='')

def complete():
    print(" Done!")
