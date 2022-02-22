def all_root5(x, y):
    return [
        (x-2, y+1),
        (x-1, y+2),
        (x-2, y-1),
        (x-1, y-2),
        (x+2, y+1),
        (x+1, y+2),
        (x+2, y-1),
        (x+1, y-2),
        ]

x1, y1, x2, y2 = map(int, input().split())

point_list1 = set(all_root5(x1, y1))
point_list2 = set(all_root5(x2, y2))
intersection = point_list1 & point_list2
if len(intersection) > 0:
    print("Yes")
else:
    print("No")