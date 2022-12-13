from collections import defaultdict, deque
import numpy as np
import heapq
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt


def parse_single_int(use_test_file=False):
    # one int per line
    if use_test_file:
        filename = "test_data.txt"
    else:
        filename = "data.txt"
    with open(filename, "r") as f:
        data = f.readlines()
    arr = [int(i) for i in data]
    return arr


def parse_single_string(use_test_file=False):
    # one string per line
    if use_test_file:
        filename = "test_data.txt"
    else:
        filename = "data.txt"
    with open(filename, "r") as f:
        data = f.readlines()
    arr = [a.replace("\n", "") for a in data]
    return arr


def parse_multi_string(use_test_file=False, sep=" "):
    # multiple strings per line
    if use_test_file:
        filename = "test_data.txt"
    else:
        filename = "data.txt"
    with open(filename, "r") as f:
        data = f.readlines()
    if sep == "":
        arr = [list(a.replace("\n", "")) for a in data]
    else:
        arr = [a.replace("\n", "").split(sep) for a in data]
    return arr


def parse_multi_int(use_test_file=False, sep=" "):
    # multiple ints per line
    if use_test_file:
        filename = "test_data.txt"
    else:
        filename = "data.txt"
    with open(filename, "r") as f:
        data = f.readlines()
    if sep == "":
        arr = [[int(i) for i in list(a.replace("\n", ""))] for a in data]
    else:
        arr = [[int(i) for i in a.replace("\n", "").split(sep)] for a in data]
    return arr


def parse_01(use_test_file=False, zero_char=".", one_char="#"):
    arr = parse_multi_string(use_test_file, sep="")
    arr_out = []
    translate = {zero_char: 0, one_char: 1}
    for a in arr:
        arr_out.append([translate[ch] for ch in a])
    return arr_out


def parse_graph(arr, symmetric=False):
    # arr is iterable of 2-element iterables
    edge_dict = defaultdict(lambda: [])
    for a, b in arr:
        edge_dict[a].append(b)
        if symmetric:
            edge_dict[b].append(a)
    return edge_dict


def shortest_path(edge_dict, from_node, to_node):
    # edge dict should be a dictionary where keys are nodes and values are dictionaries
    # edge_dict[node1][node1] = weight of edge between node 1 and node 2
    # Dijkstra's algorithm using priority queue.
    # First member of tuple denotes validity, 0 = valid, 1 = invalid, so that we can
    # update priorities as described here:
    # https://docs.python.org/3.6/library/heapq.html#priority-queue-implementation-notes
    nodes = list(edge_dict.keys())
    unvisited = [[0, 0, from_node]] + [[0, np.inf, n] for n in nodes if n != from_node]
    heapq.heapify(unvisited)
    unvisited_map = {n: unvisited[i] for i, n in enumerate(nodes)}
    dist_map = {n: np.inf for n in nodes}
    dist_map[from_node] = 0
    while len(unvisited_map) > 0:
        _, dist, node = heapq.heappop(unvisited)
        if node not in unvisited_map:
            continue
        for neighbour in edge_dict[node]:
            if neighbour in unvisited_map:
                new_dist = dist_map[node] + edge_dict[node][neighbour]
                if new_dist < dist_map[neighbour]:
                    old_queue_member = unvisited_map[neighbour]
                    old_queue_member[0] = 1  # mark invalid
                    new_queue_member = [0, new_dist, neighbour]
                    heapq.heappush(unvisited, new_queue_member)
                    unvisited_map[neighbour] = new_queue_member
                    dist_map[neighbour] = new_dist
        if node == to_node:
            break
        unvisited_map.pop(node)

    return dist_map[to_node]


def shortest_path_unweighted(edges, start, end):
    # use breadth-first search
    # edges is a dict mapping each edge to a list of its neighbours
    visited = set()
    to_visit = deque([[start, 0]])
    while len(to_visit) > 0:
        curr, dist = to_visit.popleft()
        if curr not in visited:
            visited.add(curr)
            for neighbour in edges[curr]:
                if neighbour == end:
                    return dist + 1
                if neighbour not in visited:
                    to_visit.append([neighbour, dist + 1])
    return np.inf


def connected_components(edge_dict):
    nodes = list(edge_dict.keys())
    visited = set()
    components = []
    for node in nodes:
        if node in visited:
            continue
        # use depth-first search to find connected component of this node
        curr_component = []
        to_visit = [node]
        while len(to_visit) > 0:
            node = to_visit.pop()
            if node not in visited:
                visited.add(node)
                curr_component.append(node)
            for neighbour in edge_dict[node]:
                if neighbour not in visited:
                    to_visit.append(neighbour)
        components.append(curr_component)
    return components


def binary_search(arr, condition):
    left = 0
    right = len(arr)
    while right - left > 1:
        mid = left + (right - left) // 2
        if condition(arr[mid]):
            right = mid
        else:
            left = mid
    if condition(arr[left]):
        return left
    else:
        return left + 1


def show_image(arr):
    arr = np.array(arr)
    plt.imshow(arr, origin="upper")


ALPHABET = list("abcdefghijklmnopqrstuvwxyz")

