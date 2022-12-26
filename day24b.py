from utilities import parse_multi_string
import math

arr = parse_multi_string(sep="")
arr = [a[1:-1] for a in arr[1:-1]]
width = len(arr[0])
height = len(arr)
cycle = math.lcm(width, height)

# positions repeat every cycle steps
positions = {t: [] for t in range(cycle)}
dirs = {">": 1, "<": -1, "^": 0+1j, "v": 0 - 1j}
for t in range(cycle):
    for row in range(height):
        for col in range(width):
            if (space := arr[row][col]) in dirs:
                d = dirs[space]
                real = (col + d.real * t) % width
                imag = (row - d.imag * t) % height
                positions[t].append(complex(real, -imag))

set_positions = {t: set(p) for t, p in positions.items()}


def get_distance(start, end, start_cycle):
    visited = set()
    t = 0
    dist_t = {(start, start_cycle)}
    while True:
        new_dist_t = set()
        for curr, curr_c in dist_t:
            for move in [0, 1, -1, 0 + 1j, 0 - 1j]:
                next = curr + move
                next_c = (curr_c + 1) % cycle
                if next == end:
                    return t + 1, next_c
                in_range = ((0 <= next.real < width) and (-height < next.imag <= 0)) or next == start
                if in_range and (next, next_c) not in visited and next not in set_positions[next_c]:
                    new_dist_t.add((next, next_c))
        t += 1
        dist_t = new_dist_t


start = 0 + 1j
end = complex(width - 1, -height)
d0, cycle0 = get_distance(start, end, 0)
d1, cycle1 = get_distance(end, start, cycle0)
d2, cycle2 = get_distance(start, end, cycle1)

print(d0 + d1 + d2)
