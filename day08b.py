from utilities import *

arr = parse_multi_int(sep="")
arr = np.array(arr)


def get_scores(a):
    scores = np.zeros(len(a), int)
    last_index_of_height = [0 for i in range(10)]
    for i, x in enumerate(a):
        if (i == 0) or (i == len(a) - 1):
            scores[i] = 0
            continue
        last_blocker = max([last_index_of_height[i] for i in range(x, 10)])
        scores[i] = i - last_blocker
        last_index_of_height[x] = i
    return scores


scores = np.ones(arr.shape, int)
for i in range(arr.shape[0]):
    curr_scores = get_scores(arr[i, :])
    scores[i, :] *= curr_scores
    curr_scores = get_scores(np.flip(arr[i, :]))
    scores[i, :] *= np.flip(curr_scores)
for i in range(arr.shape[1]):
    curr_scores = get_scores(arr[:, i])
    scores[:, i] *= curr_scores
    curr_scores = get_scores(np.flip(arr[:, i]))
    scores[:, i] *= np.flip(curr_scores)

best_score = np.max(scores)

print(best_score)
