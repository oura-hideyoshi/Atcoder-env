N = int(input())
S = input()

from collections import deque
_max=len(S)
ans = deque([_max])

for idx, s in enumerate(S[::-1]):
    if s=="L":
        ans.append(_max-(idx+1))
    else:
        ans.appendleft(_max-(idx+1))
print(*ans)