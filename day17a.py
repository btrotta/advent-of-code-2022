from utilities import parse_multi_string

jets = parse_multi_string(sep="")[0]

# left and right are -ve and +ve i
# down is -ve j
pattern_heights = [0, 2, 2, 3, 1]
pattern_widths = [3, 2, 2, 0, 1]


def coord_list(pattern_num, origin):
    # given coord of top left of pattern, return set of coords of rock
    if pattern_num == 0:
        return set([origin + x for x in range(4)])
    elif pattern_num == 1:
        return set([origin + 1, origin + 1 - 2j] + [origin - 1j + x for x in [0, 1, 2]])
    elif pattern_num == 2:
        return set([origin - 2j + x for x in [0, 1, 2]] + [origin + 2, origin + 2 - 1j])
    elif pattern_num == 3:
        return set([origin - complex(0, y) for y in range(4)])
    elif pattern_num == 4:
        return set([origin + complex(x, y) for x in [0, 1] for y in [0, -1]])


def move_left(pattern_num, curr_loc, filled):
    # curr_loc is location of top-left corner of pattern
    new_loc = curr_loc - 1
    if new_loc.real < 0:
        return curr_loc
    new_coords = coord_list(pattern_num, new_loc)
    if len(new_coords.intersection(filled)) == 0:
        return new_loc
    return curr_loc


def move_right(pattern_num, curr_loc, filled):
    new_loc = curr_loc + 1
    if new_loc.real + pattern_widths[pattern_num] > 6:
        return curr_loc
    new_coords = coord_list(pattern_num, new_loc)
    if len(new_coords.intersection(filled)) == 0:
        return new_loc
    return curr_loc


def move_down(pattern_num, curr_loc, filled):
    new_loc = curr_loc - 1j
    if (new_loc - complex(0, pattern_heights[pattern_num])).imag < 0:
        return curr_loc
    new_coords = coord_list(pattern_num, new_loc)
    if len(new_coords.intersection(filled)) == 0:
        return new_loc
    return curr_loc


filled = set()
curr_height = 0
step = 0
for i in range(2022):
    pattern_num = i % 5
    curr = complex(2, curr_height + 3 + pattern_heights[pattern_num])
    curr_step = 0
    while True:
        if curr_step % 2 == 0:
            jet = jets[step % len(jets)]
            if jet == "<":
                move = move_left
            else:
                move = move_right
            step += 1
        else:
            move = move_down
        curr_step += 1
        new = move(pattern_num, curr, filled)
        if move == move_down and new == curr:
            filled.update(coord_list(pattern_num, curr))
            break
        curr = new
    curr_height = 0 if len(filled) == 0 else max([x.imag for x in filled]) + 1

print(int(curr_height))
