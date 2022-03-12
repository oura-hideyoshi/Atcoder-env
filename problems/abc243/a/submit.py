V, A, B, C = map(int, input().split())

V = V - (V // (A+B+C)) * (A+B+C)

if V < A:
    print("F")
    exit()
if V - A < B:
    print("M")
    exit()

if V - A - B < C:
    print("T")
    exit()
    