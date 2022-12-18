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


def drop_rock(jet_ind, pattern_num, filled, curr_height):
    curr = complex(2, curr_height + 3 + pattern_heights[pattern_num])
    curr_step = 0
    while True:
        if curr_step % 2 == 0:
            jet = jets[jet_ind]
            if jet == "<":
                move = move_left
            else:
                move = move_right
            jet_ind = (jet_ind + 1) % len(jets)
        else:
            move = move_down
        curr_step += 1
        new = move(pattern_num, curr, filled)
        if move == move_down and new == curr:
            filled.update(coord_list(pattern_num, curr))
            break
        curr = new
    return jet_ind, new


def rebaseline(new_coords, filled):
    for c in new_coords:
        if all([complex(x, c.imag) in filled or complex(x, c.imag + 1) in filled for x in range(7)]):
            return c.imag
        elif all([complex(x, c.imag) in filled or complex(x, c.imag - 1) in filled for x in range(7)]):
            return c.imag - 1
    return None


# find a repeating pattern
filled = set()
jet_ind = 0
fill_patterns = set()
# key: pattern number, jet index, current fill pattern above baseline
# value: step, height when the pattern was encountered
state = {}
total_height = 0
curr_height = 0  # height above current baseline
step = 0
while True:
    pattern_num = step % 5
    jet_ind, curr = drop_rock(jet_ind, pattern_num, filled, curr_height)
    new_coords = coord_list(pattern_num, curr)
    filled.update(coord_list(pattern_num, curr))
    curr_height = 0 if len(filled) == 0 else max([x.imag for x in filled]) + 1
    new_baseline = rebaseline(new_coords, filled)
    if new_baseline is not None:
        filled = set([c - complex(0, new_baseline) for c in filled if c.imag >= new_baseline])
        fill_pattern = tuple(sorted(filled, key=lambda x: [x.real, x.imag]))
        total_height += new_baseline
        curr_height -= new_baseline
        # check if we have seen this state before
        state_key = (pattern_num, jet_ind, fill_pattern)
        if state_key in state:
            start_step, start_height = state[state_key]
            step_jump = step - start_step
            height_jump = total_height + curr_height - start_height
            break
        else:
            state[state_key] = (step, total_height + curr_height)
    step += 1

# simulate rock falls for as many copies of the repeating pattern as possible
num_repeats = (1000000000000 - (start_step + 1)) // step_jump
total_height = start_height + num_repeats * height_jump - curr_height
curr_step = start_step + 1 + num_repeats * step_jump

# simulate remaining rock falls
for step in range(curr_step, 1000000000000):
    pattern_num = step % 5
    jet_ind, curr = drop_rock(jet_ind, pattern_num, filled, curr_height)
    new_coords = coord_list(pattern_num, curr)
    filled.update(coord_list(pattern_num, curr))
    new_baseline = rebaseline(new_coords, filled)
    if new_baseline is not None:
        filled = set([c - complex(0, new_baseline) for c in filled if c.imag >= new_baseline])
        curr_height -= new_baseline
        total_height += new_baseline
    curr_height = 0 if len(filled) == 0 else max([x.imag for x in filled]) + 1
total_height += curr_height
print(int(total_height))

