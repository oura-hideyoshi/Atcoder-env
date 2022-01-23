N, M = map(int, input().split())

S = input().split()
T = input().split()


idx_T = 0

for idx_S in range(0, len(S)):
    if S[idx_S] == T[idx_T]:
        print("Yes")
        idx_S += 1
        idx_T += 1
    else:
        print("No")
        idx_S += 1