from math import inf
from collections import deque

N, M = map(int, input().split())

dist = [[inf for _ in range(N+1)] for __ in range(N+1)]
for idx in range(N+1):
    dist[idx][idx] = 0

pathes = []
for _ in range(M):
    start, end, cost = list(map(int, input().split()))
    dist[start][end] = cost
    dist[end][start] = cost
    pathes.append([start, end, cost])

# ワーシャルフロイド法
for mid in range(1, N+1):
    for start in range(1, N+1):
        for end in range(1, N+1):
            dist[start][end] = min(dist[start][end], dist[start][mid] + dist[mid][end])
            dist[end][start] = min(dist[start][end], dist[start][mid] + dist[mid][end])

ans = 0
for path in pathes:
    if path[2] == dist[path[0]][path[1]]:  # 最短経路
        continue
    else:
        ans += 1

print(ans)