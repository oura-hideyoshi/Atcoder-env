import math

N, X = map(int, input().split())

dirs = input()

current = X

stack = []
for dir in dirs:
    if len(stack) == 0:
        stack.append(dir)
    else:
        if dir == "U":
            if stack[-1] in ["L", "R"]:
                stack.pop()
            else:
                stack.append(dir)
        else:
            stack.append(dir)

for dir in stack:
    if dir == "U":
        current = math.floor(current / 2)
    if dir == "R":
        current = 1 + current*2
    if dir == "L":
        current = current*2
print(current)
