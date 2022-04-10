from bisect import bisect_left


N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

choco = []
box = []
for idx in range(N):
    choco.append([A[idx], B[idx], 0, "choco"])
for idx in range(M):
    box.append([C[idx], D[idx], 1, "box"])

mix = sorted(choco+box, key= lambda x : (x[0], x[2]))
mix.reverse()

S = []
for item in mix:
    if item[2] == 1:  # box
        S.append(item[1])
        S = sorted(S)
    else:
        idx_left = bisect_left(S, item[1])
        try:
            S.pop(idx_left)
        except Exception:
            print("No")
            exit()
else:
    print("Yes")