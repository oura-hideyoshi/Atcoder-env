S = input()
a, b = map(int, input().split())

s_a = S[a-1]
s_b = S[b-1]

S = list(S)
S[b-1] = s_a
S[a-1] = s_b
S = "".join(S)
print(S)