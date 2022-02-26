S = input()



def main():

    first = 0
    last = len(S) -1

    len_last_a = 0
    for s in S[::-1]:
        if s== "a":
            len_last_a += 1
        else:
            break
    len_first_a = 0
    for s in S:
        if s== "a":
            len_first_a += 1
        else:
            break

    if len_last_a < len_first_a:
        print("No")
        return
    else:
        first += len_first_a
        last -= len_last_a
        while first < last:
            if S[first] == S[last]:
                first += 1
                last -= 1
                continue
            else:
                print("No")
                return
        print("Yes")
main()