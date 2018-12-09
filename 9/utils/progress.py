tasksTotal = 100
tasksDone = None
barWidth = 80
totalWidth = 80

def setup(tasks, width=80):
    global tasksTotal, barWidth, totalWidth
    tasksTotal = tasks
    totalWidth = width
    barWidth = totalWidth - 7 - 6

def done(done):
    global tasksDone
    tasksDone = done

    # Left border of the bar
    line = '\r┣'

    # Done section
    doneLength = round(tasksDone/tasksTotal * barWidth)
    line += '█' * doneLength

    # Todo section
    todoLength = barWidth - doneLength
    line += '━' * todoLength

    # Right border
    line += "┫ "

    # Percentage
    percentageString = str(round(tasksDone/tasksTotal * 100))
    percentagePadding = 3 - len(percentageString)
    line += ' ' * percentagePadding
    line += percentageString
    line += '%'

    # Print the line
    print(line, end='')

def complete():
    print(" Done!")
