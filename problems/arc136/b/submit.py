from collections import Counter
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ca = Counter(a)
cb = Counter(b)
if ca != cb:
    print('No')
    exit()
if max(ca.values()) >= 2:
    print('Yes')
    exit()
def f(a):
    return sum(a[i] > a[j] for i in range(n) for j in range(i))
print('Yes' if f(a) % 2 == f(b) % 2 else 'No')