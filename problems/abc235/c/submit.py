from collections import defaultdict

N, Q = map(int, input().split())
A = list(map(int, input().split()))

memo = defaultdict(list)
for idx, i in enumerate(A):
    memo[i].append(idx+1)

for _ in range(Q):
    x, k = map(int, input().split())
    if len(memo[x]) < k:
        print(-1)
    else:
        print(memo[x][k-1])