from utilities import parse_multi_string

arr = parse_multi_string()


def count_cycle(cycle, ans, X):
    if (cycle == 20) or ((cycle - 20) % 40 == 0):
        ans += X * cycle
    return cycle + 1, ans


cycle = 1
ans = 0
X = 1
for a in arr:
    if a[0] == "noop":
        cycle, ans = count_cycle(cycle, ans, X)
    else:
        cycle, ans = count_cycle(cycle, ans, X)
        cycle, ans = count_cycle(cycle, ans, X)
        X += int(a[1])
print(ans)
