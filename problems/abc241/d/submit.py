from collections import defaultdict

Q = int(input())

dic = defaultdict(int)
for _ in range(Q):
    line = list(map(int, input().split()))
    if len(line) == 2:
        [com, x] = line
    else:
        [com, x, k] = line
    
    if com == 1:
        dic[x] += 1
    
    if com == 2:
        pass
    
    if com == 3:
        pass