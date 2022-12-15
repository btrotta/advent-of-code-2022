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


def check_range(left, right, y, beacons_set):
    for x in range(left, right):
        if (x, y) not in beacons_set:
            return x
    return -1


unique_beacons = set(beacons)
max_coord = 4000001
for y in range(max_coord):
    empty_ranges = []
    for s, b in zip(sensors, beacons):
        dist = abs(b[0] - s[0]) + abs(b[1] - s[1])
        max_x_dist = dist - abs(y - s[1])
        if max_x_dist >= 0:
            empty_ranges.append([s[0] - max_x_dist, s[0] + max_x_dist + 1])

    ans = None
    if len(empty_ranges) > 0:
        empty_ranges = sorted(empty_ranges)
        curr = empty_ranges[0]
        i = 0
        if (min_left := empty_ranges[0][0]) > 0 and (x := check_range(0, min_left, y, unique_beacons)) != -1:
            ans = (x, y)
        while i < len(empty_ranges):
            left, right = empty_ranges[i]
            while i + 1 < len(empty_ranges) and empty_ranges[i + 1][0] <= right:
                i += 1
                right = max(right, empty_ranges[i][1])
            else:
                i += 1
                if i < len(empty_ranges) and (x := check_range(right, empty_ranges[i][0], y, unique_beacons)) != -1:
                    ans = (x, y)
        if right < max_coord and (x := check_range(right, max_coord, y, unique_beacons)) != -1:
            ans = (x, y)
    if ans is not None:
        break

print(ans[0] * 4000000 + ans[1])
