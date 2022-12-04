from utilities import *

arr = parse_multi_string()

shape_score = {"X": 1, "Y": 2, "Z": 3}
round_score = defaultdict(lambda : 0)
round_score.update({("A", "X"): 3,
               ("B", "Y"): 3,
               ("C", "Z"): 3,
               ("A", "Y"): 6,
               ("B", "Z"): 6,
               ("C", "X"): 6})

score = 0
for x, y in arr:
    score += round_score[x, y] + shape_score[y]

print(score)