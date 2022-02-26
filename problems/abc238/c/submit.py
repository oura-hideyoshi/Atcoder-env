N = int(input())

def func(n):
    dig_n = len(str(n))
    return n - 10**(dig_n-1)+1

DEG = len(str(N))
def sum(n):
    return n*(n+1)//2

ans = 0
# 1つしたの桁までの和
for deg in range(1, DEG):
    minimam = 10**(deg-1)
    maximam = 10**deg - 1
    num = maximam - minimam +1
    sub = 10 ** (deg -1) -1
    
    left = sum(maximam) - sum(minimam-1)
    right = sub * num
    ans += left - right

if DEG == 1:
    print(sum(N))
    exit()

# その桁の和

minimam = 10**(deg)
maximam = N
num = maximam - minimam +1
sub = 10 ** (deg) -1
    
left = sum(maximam) - sum(minimam-1)
right = sub * num
ans += left - right
ans = ans % 998244353
    
print(int(ans))