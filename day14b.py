from utilities import parse_multi_string
from itertools import chain

arr_str = parse_multi_string(sep="->")
arr = []
for a in arr_str:
    arr.append([])
    for b in a:
        x, y = b.split(",")
        arr[-1].append(complex(int(x), int(y)))

all_pairs = list(chain.from_iterable(arr))
max_y = max([a.imag for a in all_pairs]) + 2

# set of filled spaces
filled = set()
for a in arr:
    for i in range(1, len(a)):
        prev, curr = a[i - 1], a[i]
        diff = curr - prev
        abs_diff = int(abs(diff))
        increment = diff / abs_diff
        for k in range(0, abs_diff + 1):
            filled.add(prev + increment * k)

ans = 0
while True:
    curr = complex(500, 0)
    while curr.imag < max_y - 1:
        if (new := curr + 1j) not in filled:
            curr = new
        elif (new := curr - 1 + 1j) not in filled:
            curr = new
        elif (new := curr + 1 + 1j) not in filled:
            curr = new
        else:
            break
    filled.add(curr)
    ans += 1
    if curr.imag == 0:
        break

print(ans)
