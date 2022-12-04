from utilities import *

arr = parse_multi_string()


def shape_score(ind):
    return ind + 1


def round_score(ind1, ind2):
    if ind1 == ind2:
        return 3
    elif (ind2 - 1) % 3 == ind1:
        return 6
    else:
        return 0


def choose_play(ind, outcome):
    if outcome == "draw":
        return ind
    elif outcome == "win":
        return (ind + 1) % 3
    else:
        return (ind - 1) % 3


score = 0
outcomes = {"X": "lose", "Y": "draw", "Z": "win"}
for x, y in arr:
    outcome = outcomes[y]
    x_ind = list("ABC").index(x)
    y_ind = choose_play(x_ind, outcome)
    score += shape_score(y_ind) + round_score(x_ind, y_ind)

print(score)
