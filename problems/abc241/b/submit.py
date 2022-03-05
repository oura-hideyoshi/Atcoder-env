from collections import Counter

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_count = Counter(A)
B_count = Counter(B)

for b in B_count:
    if B_count[b] <= A_count[b]:
        continue
    else:
        print("No")
        exit()
else:
    print("Yes")