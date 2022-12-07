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


ans = 0
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
        if (node.size_below <= 100000) and (len(node.contents) > 0):
            ans += node.size_below

print(ans)
