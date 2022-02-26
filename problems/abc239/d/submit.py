A, B, C, D = map(int, input().split())

def prime(N):
    primes = []
    for i in range(2, N + 1):
        primes.append(i)
        for p in range(2, i):
            if i % p == 0:
                primes.remove(i)
                break
    return primes
prime_list = prime(200)

is_taka_win = False
for taka in range(A, B+1): # ある数について
    for aoki in range(C, D+1): # どの数を加えても素数にならなければ高橋の勝ち
        if taka + aoki in prime_list:
            break
    else:
        is_taka_win = True
        break
    
if is_taka_win:
    print("Takahashi")
else:
    print("Aoki")