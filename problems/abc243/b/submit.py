N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans_a = 0
ans_b = 0
set_b = set(B)

for idx in range(N):
    if set_b.__contains__(A[idx]):
        if A[idx] == B[idx]:
            ans_a += 1
        else:
            ans_b += 1
print(ans_a)
print(ans_b)
        