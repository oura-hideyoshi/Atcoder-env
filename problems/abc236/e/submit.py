N = int(input())

A = list(map(int, input().split()))

# average
dp = [[0, 0] for _ in range(N)]
dp[0] = [A[0], 1]
if dp[0][0] < sum(A[:2])/2:
    dp[1] = [sum(A[:2])/2, 2]
else:
    dp[1] = [A[0], 1]

ans = max(dp[0][0], dp[1][0])
for idx in range(2, len(A)):
    _sum = dp[idx-2][0]*dp[idx-2][1] + A[idx]
    in_past2 = _sum / (dp[idx-2][1] +1)
    _sum = dp[idx-1][0]*dp[idx-1][1] + A[idx]
    in_past1 = _sum / (dp[idx-1][1] +1)
    if in_past1 < in_past2:
        dp[idx][0] = in_past2
        dp[idx][1] = dp[idx-2][1] +1
    else:
        dp[idx][0] = in_past1
        dp[idx][1] = dp[idx-1][1] +1
    ans = max(ans, dp[idx][0])
print(ans)