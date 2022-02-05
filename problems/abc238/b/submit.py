N = int(input())
lines = list(map(int, input().split()))

degs = [0, 360]
current = 0

for line in lines:
    current = (current + line) % 360
    degs.append(current)

degs = sorted(degs)

ans = 0
for idx in range(N+1):
    ans = max(abs(degs[idx] - degs[idx+1]), ans)
print(ans)