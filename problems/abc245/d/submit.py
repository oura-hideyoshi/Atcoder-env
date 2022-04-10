N, M = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))

B = [0 for _ in range(M+1)]

A.reverse()
C.reverse()

for b_digit in range(M+1):
    B[b_digit] = C[b_digit] // A[0]
    
    for a_digit, a in enumerate(A):
        c_digit = b_digit + a_digit
        C[c_digit] = C[c_digit] - B[b_digit] * A[a_digit]

B.reverse()
print(*B)
    