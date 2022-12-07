from utilities import *

arr = parse_multi_string(sep=" ")


class Node:

    def __init__(self, index, parent=None, size=0):
        self.index = index
        self.parent = parent
        self.contents = {}
        self.size = size
        self.size_below = size


root = Node(0)
index = 1
node_dict = {}

curr = root
for i, line in enumerate(arr):
    if line[0] == "$":
        if line[1] == "cd":
            if line[2] == "..":
                curr = curr.parent
            else:
                dirname = line[2]
                if dirname == "/":
                    curr = root
                else:
                    curr = curr.contents[dirname]
    else:
        if line[0] == "dir":
            dirname = line[1]
            node_dict[index] = Node(index, parent=curr)
            curr.contents[dirname] = node_dict[index]
            index += 1
        else:
            size = int(line[0])
            filename = line[1]
            node_dict[index] = Node(index, parent=curr, size=size)
            curr.contents[filename] = node_dict[index]
            index += 1


# get total size
to_visit = [root]
visited = set()
while len(to_visit) > 0:
    node = to_visit[-1]
    for sub in node.contents.values():
        if sub.index not in visited:
            to_visit.append(sub)
            break
    else:
        node = to_visit.pop()
        visited.add(node.index)
        if node.parent is not None:
            node.parent.size_below += node.size_below

total_used = root.size_below
total_free = 70000000 - total_used
amount_to_delete = 30000000 - total_free

# find smallest directory to delete
ans = root.size_below
for index, node in node_dict.items():
    if (len(node.contents) > 0) and (node.size_below < ans) and (node.size_below >= amount_to_delete):
        ans = node.size_below

print(ans)
