from utilities import parse_multi_int

arr = parse_multi_int(sep=",")
arr = set([tuple(a) for a in arr])
ans = 0
for x, y, z in arr:
    adj = {(x - 1, y, z), (x + 1, y, z), (x, y - 1, z), (x, y + 1, z), (x, y, z - 1), (x, y, z + 1)}
    ans += len(adj.difference(arr))

print(ans)
