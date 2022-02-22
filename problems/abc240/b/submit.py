from collections import Counter

N = int(input())
L = map(int, input().split())
S = Counter(L)
print(len(S))