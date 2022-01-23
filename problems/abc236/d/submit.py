N = int(input())

aisho = []
for _ in range(2*N-1):
    aisho.append(list(map(int, input().split())))

combinations = []
def combi(member, combi_member):
    if len(member) == 2:
        combi_member.append([*member])
        combinations.append(combi_member)
        return
    member = sorted(member)
    for m in member[1:]:
        first = member[0]
        _member = member[1:]
        _member.remove(m)
        _combi_member = combi_member.copy()
        _combi_member.append([first, m])
        combi(_member, _combi_member)

member = list(range(2*N))
combi(member, [])
# print(*combinations)

for com in combinations:
    for cupple in com:
        love = []
        love.append(aisho[cupple[1]][cupple[0]])
    pass
