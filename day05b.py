from utilities import *

arr = parse_single_string()

# find stack labels
for line_num, a in enumerate(arr):
    if a[1] == "1":
        break

num_stacks = int(a[-1])

stacks = [[] for i in range(num_stacks)]
for a in arr[:line_num]:
    for i in range(num_stacks):
        if 4 * i + 1 < len(a):
            ch = a[4 * i + 1]
            if ch != " ":
                stacks[i].append(ch)

stacks = [list(reversed(s)) for s in stacks]

moves = []
for a in arr[line_num + 2:]:
    words = a.split(" ")
    curr_move = []
    for w in words:
        try:
            curr_move.append(int(w))
        except:
            pass
    moves.append(curr_move)


for num, source, dest in moves:
    to_move = stacks[source - 1][-num:]
    stacks[source - 1] = stacks[source - 1][:-num]
    stacks[dest - 1] += to_move


print("".join([s[-1] for s in stacks]))

