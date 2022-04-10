A, B, C, D = map(int, input().split())

if A > C:
    print("Aoki")
if A < C:
    print("Takahashi")
if A==C:
    if B <= D:
        print("Takahashi")
    else:
        print("Aoki")