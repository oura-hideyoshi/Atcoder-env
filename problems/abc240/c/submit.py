N, X = map(int, input().split())

memo = set([0])
for _ in range(N):
        a, b = map(int, input().split())
        new_memo = set([])
        for i in memo:
            new_memo.add(i+a)
            new_memo.add(i+b)
        memo = new_memo

if X in memo:
    print("Yes")
else:
    print("No")
