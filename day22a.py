from utilities import parse_single_string
import re
import numpy as np

arr = parse_single_string()
row_start = []
row_width = []
max_width = max([len(a) for a in arr[:-2]])
col_start = [np.inf for i in range(max_width)]
col_height = [0 for i in range(max_width)]
walls = set()
for row, a in enumerate(arr[:-2]):
    col = 0
    while a[col] == " ":
        col += 1
    row_start.append(col)
    row_width.append(len(a) - col)
    for col in range(row_start[-1], len(a)):
        col_start[col] = min(col_start[col], row)
        col_height[col] = max(col_height[col], row - col_start[col] + 1)
        ch = a[col]
        if ch == "#":
            walls.add((row, col))

dirs = re.findall("[0-9]+|[A-Z]+", arr[-1])
row, col = (0, row_start[0])
facing = "R"
directions = ["U", "R", "D", "L"]
moves = {"L": -1, "R": 1, "U": -1, "D": 1}
for d in dirs:
    if d.isdigit():
        num = int(d)
    else:
        rotate = d
        curr_dir_ind = directions.index(facing)
        if rotate == "R":
            facing = directions[(curr_dir_ind + 1) % 4]
        else:
            facing = directions[(curr_dir_ind - 1) % 4]
        continue
    move = moves[facing]
    if facing in ["L", "R"]:
        for i in range(num):
            new_col = row_start[row] + ((col - row_start[row] + move) % row_width[row])
            if (row, new_col) in walls:
                break
            col = new_col
    else:
        for i in range(num):
            new_row = col_start[col] + ((row - col_start[col] + move) % col_height[col])
            if (new_row, col) in walls:
                break
            row = new_row

facing_dict = {"R": 0, "D": 1, "L": 2, "U": 3}
ans = (row + 1) * 1000 + (col + 1) * 4 + facing_dict[facing]
print(ans)
