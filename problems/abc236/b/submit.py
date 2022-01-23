N = int(input())
nums = list(map(int, input().split()))

dic = [0]*(N+1)
for n in nums:
    dic[n] += 1

for idx, n in enumerate(dic):
    if n == 3:
        print(idx)