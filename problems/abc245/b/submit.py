N = int(input())
A = list(map(int, input().split()))

A = sorted(set(A))

ans = 0
for a in A:
    if a == ans:
        ans += 1
        continue
    else:
        break

print(ans)