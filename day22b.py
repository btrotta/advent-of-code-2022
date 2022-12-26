from utilities import *
import re

arr = parse_single_string(use_test_file=False)
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

# get length of cube sides
cube_side = int(np.sqrt((sum(row_width)) // 6))

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
    for i in range(num):
        move = moves[facing]
        if facing in ["L", "R"]:
            new_row = row
            new_col = col + move
            new_facing = facing
            if facing == "R" and new_col == row_start[row] + row_width[row]:
                if row // cube_side == 0:
                    new_row = 2 * cube_side + ((-row - 1) % cube_side)
                    new_col = 2 * cube_side - 1
                    new_facing = "L"
                elif row // cube_side == 1:
                    new_col = (row % cube_side) + 2 * cube_side
                    new_row = cube_side - 1
                    new_facing = "U"
                elif row // cube_side == 2:
                    new_row = (-row - 1) % cube_side
                    new_col = cube_side * 3 - 1
                    new_facing = "L"
                elif row // cube_side == 3:
                    new_col = cube_side + (row % cube_side)
                    new_row = 3 * cube_side - 1
                    new_facing = "U"
            elif facing == "L" and new_col == row_start[row] - 1:
                if row // cube_side == 0:
                    new_row = 2 * cube_side + ((-row - 1) % cube_side)
                    new_col = 0
                    new_facing = "R"
                elif row // cube_side == 1:
                    new_row = 2 * cube_side
                    new_col = row % cube_side
                    new_facing = "D"
                elif row // cube_side == 2:
                    new_row = (-row - 1) % cube_side
                    new_col = cube_side
                    new_facing = "R"
                elif row // cube_side == 3:
                    new_row = 0
                    new_col = cube_side + (row % cube_side)
                    new_facing = "D"
        else:
            new_row = row + move
            new_col = col
            new_facing = facing
            if facing == "D" and new_row == col_start[col] + col_height[col]:
                if col // cube_side == 2:
                    new_row = cube_side + (col % cube_side)
                    new_col = cube_side * 2 - 1
                    new_facing = "L"
                elif col // cube_side == 1:
                    new_row = cube_side * 3 + (col % cube_side)
                    new_col = cube_side - 1
                    new_facing = "L"
                elif col // cube_side == 0:
                    new_row = 0
                    new_col = cube_side * 2 + col
                    new_facing = "D"
            elif facing == "U" and new_row == col_start[col] - 1:
                if col // cube_side == 0:
                    new_row = cube_side + col
                    new_col = cube_side
                    new_facing = "R"
                elif col // cube_side == 1:
                    new_row = cube_side * 3 + (col % cube_side)
                    new_col = 0
                    new_facing = "R"
                elif col // cube_side == 2:
                    new_row = 4 * cube_side - 1
                    new_col = col % cube_side
                    new_facing = "U"
        if (new_row, new_col) in walls:
            break
        row, col, facing = new_row, new_col, new_facing

facing_dict = {"R": 0, "D": 1, "L": 2, "U": 3}
ans = (row + 1) * 1000 + (col + 1) * 4 + facing_dict[facing]
print(ans)
