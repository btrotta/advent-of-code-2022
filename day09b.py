from utilities import parse_multi_string

arr = parse_multi_string()
arr = [[a[0], int(a[1])] for a in arr]


def sign(x):
    return 1 if x > 0 else -1


def distance(leader_coords, follower_coords):
    return [leader_coords[0] - follower_coords[0], leader_coords[1] - follower_coords[1]]


def follow(leader_coords, follower_coords, follower_positions=None):
    dist = distance(leader_coords, follower_coords)
    dist_sign = [sign(dist[0]), sign(dist[1])]
    if max(abs(dist[0]), abs(dist[1])) <= 1:
        return
    if (abs(dist[0]) >= 1) and (abs(dist[1]) >= 1):
        # diagonal move
        follower_coords[0] += dist_sign[0]
        follower_coords[1] += dist_sign[1]
        if follower_positions:
            follower_positions.add(tuple(follower_coords))
    else:
        # move in direction of sign along axis having distance > 1
        axis = 0 if abs(dist[0]) > 1 else 1
        follower_coords[axis] += dist_sign[axis]
        if follower_positions:
            follower_positions.add(tuple(follower_coords))


tail_positions = {(0, 0)}
knot_coords = [[0, 0] for i in range(10)]
# map moves to axis and sign
moves = {"L": (0, -1), "R": (0, 1), "U": (1, 1), "D": (1, -1)}
for move_dir, num in arr:
    axis, move_sign = moves[move_dir]
    for step in range(num):
        knot_coords[0][axis] += move_sign
        for i in range(1, 10):
            follower_positions = tail_positions if i == 9 else None
            follow(knot_coords[i - 1], knot_coords[i], follower_positions)

print(len(tail_positions))
