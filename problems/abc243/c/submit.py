from warnings import catch_warnings


N = int(input())

men = []
for _ in range(N):
    men.append(list(map(int, input().split())) + [_])

directions = input()

men = sorted(men, key=lambda x: (x[1], x[0]))

idx = 0
while idx < N:
    first = men[idx]
    row = [directions[first[2]]]
    while True:
        idx += 1
        try:
            if first[1] == men[idx][1]:
                row.append(directions[men[idx][2]])
            else:
                break
        except Exception:
            break
    
    if len(row)  >= 2:
        for _idx, _ in enumerate(row[:-1]):
            if row[_idx] == "R" and row[_idx+1] == "L":
                print("Yes")
                exit()
    else:
        continue
else:
    print("No")