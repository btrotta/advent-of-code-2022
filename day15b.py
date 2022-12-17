from utilities import parse_single_string
import numpy as np
from itertools import product

arr = parse_single_string()
sensors = []
beacons = []
for a in arr:
    words = a.split(" ")
    sensors.append(complex(int(words[2][2:-1]), int(words[3][2:-1])))
    beacons.append(complex(int(words[8][2:-1]), int(words[9][2:])))


def distance(a, b):
    return abs(a.real - b.real) + abs(a.imag - b.imag)


def find_intersection(s1, d1, s2, d2):
    intersections = []
    for s1_real_sign, s1_imag_sign, s2_real_sign, s2_imag_sign in product([1, -1], repeat=4):
        rhs1 = d1 + s1_real_sign * s1.real + s1_imag_sign * s1.imag
        rhs2 = d2 + s2_real_sign * s2.real + s2_imag_sign * s2.imag
        X = np.matrix([[s1_real_sign, s1_imag_sign], [s2_real_sign, s2_imag_sign]])
        y = np.matrix([[rhs1], [rhs2]])
        try:
            x, y = np.linalg.solve(X, y)
            intersections.append(complex(x[0][0], y[0][0]))
        except:
            pass
    return intersections


distances = [distance(s, b) for s, b in zip(sensors, beacons)]
max_coord = 4000000
ans = None
# check corners of range
for curr in [complex(0, 0), complex(0, max_coord), complex(max_coord, 0), complex(max_coord, max_coord)]:
    if all([distance(curr, s) > d for s, d in zip(sensors, distances)]):
        ans = curr
        break
# check intersections
for s1, d1 in zip(sensors, distances):
    if ans is not None:
        break
    for s2, d2 in zip(sensors, distances):
        if ans is not None:
            break
        intersections = find_intersection(s1, d1, s2, d2)
        for a in intersections:
            for increment in [1, -1, 0+1j, 0-1j, 1+1j, 1-1j, -1+1j, -1-1j]:
                curr = a + increment
                in_range = curr.real >= 0 and curr.imag >= 0 and curr.real <= max_coord and curr.imag <= max_coord
                if in_range and all([distance(curr, s) > d for s, d in zip(sensors, distances)]):
                        ans = curr
                        break

print(int(ans.real * 4000000 + ans.imag))
