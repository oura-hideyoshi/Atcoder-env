N = int(input())

mat = [[0 for _ in range(N)] for __ in range(N)]
for idx in range(N):
    mat[idx] = [0 if s == "." else 1 for s in list(input())]

def can_connect6(line):
    if len(line) < 6:
        return False

    left = 0
    count = line[0:6].count(1)
    if 4 <= count:
        return True

    for right in range(6, len(line)):
        
        if line[right] == 1 and line[left] == 0:
            count += 1
        if line[right] == 0 and line[left] == 1:
            count -= 1
        left += 1
        
        if 4 <= count:
            return True
    else:
        return False

# # horizon
for y in range(N):
    if can_connect6(mat[y]):
        print("Yes")
        exit()
# # vertical
for x in range(N):
    line = [mat[y][x] for y in range(N)]
    if can_connect6(line):
        print("Yes")
        exit()
# 左下から右上
for init_y in range(N):
    line = [mat[init_y - inc][0 + inc] for inc in range(init_y+1)]
    if can_connect6(line):
        print("Yes")
        exit()
    line = [mat[N-1 - inc][N-1 - init_y + inc] for inc in range(init_y + 1)]
    if can_connect6(line):
        print("Yes")
        exit()

# 左上から右下
for init_y in range(N):
    line = [mat[init_y + inc][0 + inc] for inc in range(N-1 - init_y+1)]
    if can_connect6(line):
        print("Yes")
        exit()
    line = [mat[0 + inc][init_y + inc] for inc in range(N-1 - init_y+1)]
    if can_connect6(line):
        print("Yes")
        exit()

print("No")
