from utilities import parse_single_string, ALPHABET
import numpy as np

arr = parse_single_string()

priorities = {ch: i + 1 for i, ch in enumerate(ALPHABET)}
priorities.update({ch.upper(): i + 27 for i, ch in enumerate(ALPHABET)})

ans = 0
for a in arr:
    common = np.intersect1d(list(a[:len(a)//2]), list(a[len(a)//2:]))[0]
    ans += priorities[common]

print(ans)
