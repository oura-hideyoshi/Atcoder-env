N = int(input())

for _ in range(N):
    a, s = map(int, input().split())
    bin_a = ("0"*60+format(a, "b"))[-60:]
    bin_s = ("0"*60+format(s, "b"))[-60:]

    x = a
    bin_x = ("0"*60+format(x, "b"))[-60:]
    sub = s - 2*x
    bin_sub = ("0"*60+format(sub, "b"))[-60:]
    
    if sub < 0:
        print("No")
        continue
    
    for idx, bin in enumerate(bin_sub):
        if bin == "1":
            if bin_x[idx] == "0":
                continue
            else:
                print("No")
                break
    else:
        print("Yes")
    
    
