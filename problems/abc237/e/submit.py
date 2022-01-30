from collections import deque
from math import inf

N, M = map(int, input().split())
H = list(map(int, input().split()))

vm = [[int(_) for _ in input().split()] for i in range(M)]
load = [[] for _ in range(2*10**5 +1)]

for v, m in vm:
    load[v].append(m)
    load[m].append(v)

queue = deque([1])
costs = [-inf for _ in range(N+1)] 
costs[1] = 0
ans = 0
while len(queue) != 0:
    here = queue.popleft()
    here_height = H[here - 1]
    here_cost = costs[here]
    for to in load[here]:
        to_height = H[to-1]
        to_cost = costs[to]
        
        happiness = 0
        if here_height < to_height:
            happiness = -2*abs(here_height - to_height)
        else:
            happiness = here_height - to_height
        
        if to_cost < here_cost + happiness:
            costs[to] = here_cost + happiness
            ans = max(ans, costs[to])
            queue.append(to)
print(ans)
    