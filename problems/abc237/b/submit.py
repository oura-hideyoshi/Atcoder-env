H, W = map(int, input().split())

mat = [[int(_) for _ in input().split()] for i in range(H)]

ans = [[0 for _ in range(H)] for __ in range(W)]

for y, col in enumerate(mat):
    for x, v in enumerate(col):
        ans[x][y] = v

for col in ans:
    print(*col)
