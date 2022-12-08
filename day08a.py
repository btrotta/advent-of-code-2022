from utilities import parse_multi_int
import numpy as np

arr = parse_multi_int(sep="")
arr = np.array(arr)


def get_visible(a, index):
    visible = []
    curr_max = -1
    for i, x in enumerate(a):
        if x > curr_max:
            visible.append(index[i])
            curr_max = x
    return visible


index = np.reshape(np.arange(arr.size), arr.shape)
visible = set()
for i in range(arr.shape[0]):
    visible = visible.union(get_visible(arr[i, :], index[i, :]))
    visible = visible.union(get_visible(np.flip(arr[i, :]), np.flip(index[i, :])))
for i in range(arr.shape[1]):
    visible = visible.union(get_visible(arr[:, i], index[:, i]))
    visible = visible.union(get_visible(np.flip(arr[:, i]), np.flip(index[:, i])))

print(len(visible))
