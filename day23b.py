from utilities import parse_01
from collections import Counter

arr = parse_01()
elves = set()
for row in range(len(arr)):
    for col in range(len(arr[0])):
        if arr[row][col] == 1:
            elves.add(complex(col, -row))

dirs = {"N": 0 + 1j, "E": 1, "S": 0 - 1j, "W": -1}
dir_checks = {"N": [0 + 1j, 1 + 1j, -1 + 1j],
              "E": [1, 1 - 1j, 1 + 1j],
              "S": [0 - 1j, 1 - 1j, -1 - 1j],
              "W": [-1, -1 - 1j, -1 + 1j]}
all_dirs = [0 + 1j, 0 - 1j, -1, 1, 1 + 1j, 1 - 1j, -1 + 1j, -1 - 1j]
dir_list = ["N", "S", "W", "E"]
round = 0
any_move = True
while any_move:
    proposed_locations = {}
    loc_count = Counter()
    for e in elves:
        if all([e + diff not in elves for diff in all_dirs]):
            continue
        for dir_offset in range(4):
            dir_ind = (dir_offset + round) % 4
            d = dir_list[dir_ind]
            new_loc = e + dirs[d]
            if all([e + diff not in elves for diff in dir_checks[d]]):
                proposed_locations[e] = new_loc
                loc_count.update([new_loc])
                break
    new_elves = set()
    any_move = False
    for e in elves:
        if e in proposed_locations:
            new_loc = proposed_locations[e]
            if loc_count[new_loc] == 1:
                new_elves.add(proposed_locations[e])
                any_move = True
            else:
                new_elves.add(e)
        else:
            new_elves.add(e)
    elves = new_elves
    round += 1

print(round)
