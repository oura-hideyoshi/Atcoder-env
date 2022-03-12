N = int(input())
S = input()

ans = []
for char in S:
    if len(ans) == 0:
        ans.append(char)
        continue
    if char == "C":
        ans.append("C")
        continue
    if ans[-1] == "C":
        ans.append(char)
        continue
    if ans[-1] == "B" and char == "A":
        ans[-1] = "A"
        ans.append("B")
        continue
    if ans[-1] == "B" and char == "B":
        ans[-1] = "A"
        continue
    if ans[-1] == "A":
        ans.append(char)
        continue
        
print("".join(ans))

