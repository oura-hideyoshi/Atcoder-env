N, Q = map(int, input().split())
X = list(map(int, input().split()))

edges = [[] for _ in range(N+1)]
memo = [[0, 0] for _ in range(N+1)]
for _ in range(N-1):
    A, B = map(int, input().split())
    A, B = sorted([A, B])
    edges[A] = sorted(edges[A] + [B])  #

stack = []
time = 0

def dfs(node):
    global time
    time += 1
    memo[node][0] = time
    stack.append(node)
    
    if len(edges[node]) == 1:
        dfs(edges[node][0])
    if len(edges[node]) == 2:
        dfs(edges[node][0])
        dfs(edges[node][1])
    
    memo[node][1] = time

dfs(1)
val = []
for idx, sta in enumerate(stack):
    val.append(X[sta-1])

for _ in range(Q):
    
    print(max(val))