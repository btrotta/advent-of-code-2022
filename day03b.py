from utilities import parse_single_string, ALPHABET
from functools import reduce
import numpy as np

arr = parse_single_string()

priorities = {ch: i + 1 for i, ch in enumerate(ALPHABET)}
priorities.update({ch.upper(): i + 27 for i, ch in enumerate(ALPHABET)})

ans = 0
for i in range(0, len(arr), 3):
    common = reduce(np.intersect1d, [list(arr[i]), list(arr[i + 1]), list(arr[i + 2])])[0]
    ans += priorities[common]

print(ans)
