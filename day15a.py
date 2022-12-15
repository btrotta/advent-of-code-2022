from utilities import parse_single_string

arr = parse_single_string()


def get_xy(s):
    words = s.split(" ")
    for w in words:
        if w.startswith("x="):
            x = int(w[2:].replace(",", ""))
        elif w.startswith("y="):
            y = int(w[2:].replace(",", ""))
    return (x, y)


sensors = []
beacons = []
for a in arr:
    s, b = a.split(":")
    sensors.append(get_xy(s))
    beacons.append(get_xy(b))

y = 2000000
empty_ranges = []
for s, b in zip(sensors, beacons):
    dist = abs(b[0] - s[0]) + abs(b[1] - s[1])
    max_x_dist = dist - abs(y - s[1])
    if max_x_dist >= 0:
        empty_ranges.append([s[0] - max_x_dist, s[0] + max_x_dist + 1])

unique_beacons = set(beacons)
empty_ranges = sorted(empty_ranges)
curr = empty_ranges[0]
ans = 0
i = 0
while i < len(empty_ranges):
    left, right = empty_ranges[i]
    while i + 1 < len(empty_ranges) and empty_ranges[i + 1][0] <= right:
        i += 1
        right = max(right, empty_ranges[i][1])
    else:
        ans += right - left - len(set([b[0] for b in unique_beacons if b[1] == y and b[0] >= left and b[1] < right]))
        i += 1
print(ans)
