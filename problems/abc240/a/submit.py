a, b = map(int, input().split())

# if abs((a % 10) - (b % 10)) == 1:
#     print("Yes")
# else:
#     print("No")

if b == a + 1 or b  == a + 9:
    print("Yes")
else:
    print("No")