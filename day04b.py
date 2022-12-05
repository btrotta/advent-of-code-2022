from utilities import *

arr = parse_multi_string(sep=",")

ans = 0
for a in arr:
    p1 = [int(x) for x in a[0].split("-")]
    p2 = [int(x) for x in a[1].split("-")]
    if max(p1[0], p2[0]) <= min(p1[1], p2[1]):
        ans += 1

print(ans)
