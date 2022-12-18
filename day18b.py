from utilities import parse_multi_int, connected_components

arr = parse_multi_int(sep=",", use_test_file=False)
arr = set([tuple(a) for a in arr])
x_coords = [a[0] for a in arr]
min_x, max_x = min(x_coords), max(x_coords)
y_coords = [a[1] for a in arr]
min_y, max_y = min(y_coords), max(y_coords)
z_coords = [a[2] for a in arr]
min_z, max_z = min(z_coords), max(z_coords)


# for each empty coord, get adjoining empty coords
edges = {}
empty_points = set()
for x in range(min_x - 1, max_x + 2):
    for y in range(min_y - 1, max_y + 2):
        for z in range(min_z - 1, max_z + 2):
            if (x, y, z) not in arr:
                empty_points.add((x, y, z))
                if (x, y, z) not in edges:
                    edges[x, y, z] = []
                for adj in [(x - 1, y, z), (x + 1, y, z), (x, y - 1, z), (x, y + 1, z), (x, y, z - 1), (x, y, z + 1)]:
                    in_cube = ((min_x - 1 <= adj[0] < max_x + 2)
                               and (min_y - 1 <= adj[1] < max_y + 2)
                               and (min_z - 1 <= adj[2] < max_z + 2))
                    if in_cube and adj not in arr:
                        edges[x, y, z].append(adj)

outside_point = (min_x - 1, min_y, min_z)
components = connected_components(edges)
inside = set()
for i, c in enumerate(components):
    for coord in c:
        if coord == outside_point:
            break
    else:
        inside.update(set(c))

ans = 0
for x, y, z in arr:
    adj = {(x - 1, y, z), (x + 1, y, z), (x, y - 1, z), (x, y + 1, z), (x, y, z - 1), (x, y, z + 1)}
    exposed_surface = adj.difference(arr)
    exposed_outside_surface = exposed_surface.difference(inside)
    ans += len(exposed_outside_surface)

print(ans)
