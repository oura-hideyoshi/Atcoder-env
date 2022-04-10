from collections import deque

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

connection = []

for idx in range(1, N):
    a, b, c, d = (0,0,0,0)
    if abs(A[idx-1] - A[idx]) <= K:
        a = 1
    if abs(A[idx-1] - B[idx]) <= K:
        b = 1
    if abs(B[idx-1] - A[idx]) <= K:
        c = 1
    if abs(B[idx-1] - B[idx]) <= K:
        d = 1
    connection.append([a,b,c,d])

from collections import defaultdict

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

UF = UnionFind(N*2)
for idx, connect in enumerate(connection):
    if connect[0] == 1:
        UF.union(idx*2, (idx+1)*2)
    if connect[1] == 1:
        UF.union(idx*2, (idx+1)*2 +1)
    if connect[2] == 1:
        UF.union(idx*2 +1, (idx+1)*2)
    if connect[3] == 1:
        UF.union(idx*2 +1, (idx+1)*2 +1)

if UF.find((N-1)*2) in [0, 1] or UF.find((N-1)*2 +1) in [0,1]:
    print("Yes")
else:
    print("No")