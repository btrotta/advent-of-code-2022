from utilities import *
from functools import reduce

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
vis_directions = []
for i in range(arr.shape[0]):
    vis_directions.append(get_visible(arr[i, :], index[i, :]))
    vis_directions.append(get_visible(np.flip(arr[i, :]), np.flip(index[i, :])))
for i in range(arr.shape[1]):
    vis_directions.append(get_visible(arr[:, i], index[:, i]))
    vis_directions.append(get_visible(np.flip(arr[:, i]), np.flip(index[:, i])))

visible = reduce(np.union1d, vis_directions)
print(len(visible))
