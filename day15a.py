from utilities import parse_single_string

arr = parse_single_string()
sensors = []
beacons = []
for a in arr:
    words = a.split(" ")
    sensors.append(complex(int(words[2][2:-1]), int(words[3][2:-1])))
    beacons.append(complex(int(words[8][2:-1]), int(words[9][2:])))

y = 2000000
empty_ranges = []
for s, b in zip(sensors, beacons):
    dist = abs(b.real - s.real) + abs(b.imag - s.imag)
    max_x_dist = dist - abs(y - s.imag)
    if max_x_dist >= 0:
        empty_ranges.append([s.real - max_x_dist, s.real + max_x_dist + 1])

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
        ans += right - left - len(set([b.real for b in unique_beacons if b.imag == y and b.real >= left and b.imag < right]))
        i += 1
print(int(ans))
