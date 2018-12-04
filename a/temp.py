def solution(lines):
    for line in lines:
        print(line)

with open("input.txt", "r") as file:
    solution(file.read().splitlines())
