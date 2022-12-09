from utilities import parse_multi_string

arr = parse_multi_string()
arr = [[a[0], int(a[1])] for a in arr]

tail_positions = {(0, 0)}
head_coords = [0, 0]
tail_coords = [0, 0]
# map moves to axis and sign
moves = {"L": (0, -1), "R": (0, 1), "U": (1, 1), "D": (1, -1)}
for move_dir, num in arr:
    axis, sign = moves[move_dir]
    head_coords[axis] += sign * num
    if abs(head_coords[axis] - tail_coords[axis]) > 1:
        if tail_coords[1 - axis] != head_coords[1 - axis]:
            # diagonal move first
            tail_coords[1 - axis] = head_coords[1 - axis]
            tail_coords[axis] += sign
            tail_positions.add(tuple(tail_coords))
        # move in direction of sign along axis
        while abs(tail_coords[axis] - head_coords[axis]) > 1:
            tail_coords[axis] += sign
            tail_positions.add(tuple(tail_coords))

print(len(tail_positions))
