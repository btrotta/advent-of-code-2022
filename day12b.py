from collections import defaultdict
from utilities import ALPHABET, parse_multi_string, shortest_path_unweighted

arr = parse_multi_string(sep="")

# convert array to numeric
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j] == "S":
            arr[i][j] = "a"
        elif arr[i][j] == "E":
            end = (i, j)
            arr[i][j] = "z"
        arr[i][j] = ALPHABET.index(arr[i][j])

edges = defaultdict(list)
for i in range(len(arr)):
    for j in range(len(arr[0])):
        for [x, y] in [[i + 1, j], [i - 1, j], [i, j - 1], [i, j + 1]]:
            if (x >= 0) and (x < len(arr)) and (y >= 0) and (y < len(arr[0])) and (arr[x][y] - arr[i][j] <= 1):
                edges[i, j].append((x, y))

starts = [[i, j] for i in range(len(arr)) for j in range(len(arr[0])) if arr[i][j] == 0]
print(min([shortest_path_unweighted(edges, tuple(start), tuple(end)) for start in starts]))