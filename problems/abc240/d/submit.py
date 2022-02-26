from collections import deque
N = int(input())

stack = deque()
balls = list(map(int, input().split()))
memo = []

for ball in balls:
    
    if len(stack) != 0:
        if stack[-1] == ball:
            stack.append(ball)
            memo[-1] += 1
            if memo[-1] == ball:
                for _ in range(ball):
                    stack.pop()
                memo.pop()
        else:
            stack.append(ball)
            memo.append(1)        
    else:
        stack.append(ball)
        memo.append(1)
    
    print(len(stack))