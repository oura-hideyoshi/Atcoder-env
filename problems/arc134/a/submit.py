from math import ceil
N, L, W = map(int, input().split())

a = list(map(int, input().split()))

current = 0
ans = 0
for boundary in a:
    if current < boundary:
        len_lack = boundary - current # 覆えない長さ
        n_sheet = ceil(len_lack / W)
        ans += n_sheet
        current = boundary + W
        
    else:
        current = boundary + W

len_lack = L - current # 覆えない長さ
n_sheet = ceil(len_lack / W)
ans += n_sheet
current = boundary + W
print(ans)