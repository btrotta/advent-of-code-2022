from functools import cmp_to_key

with open("data.txt", "r") as f:
    data = f.readlines()

strings = []
for line in data:
    if line != "\n":
        strings.append(line.replace("\n", ""))

# add divider packets
strings += ["[[2]]", "[[6]]"]


class Node:

    def __init__(self, parent=None, value=None):
        self.parent = parent
        self.children = []
        self.value = value


def str_to_tree(s):
    # convert the string representing a list to a tree and return the root
    root = Node()
    curr = root
    i = 1
    while i < len(s):
        ch = s[i]
        if ch == "[":
            new_node = Node(parent=curr)
            curr.children.append(new_node)
            curr = new_node
            i += 1
        elif ch == "]":
            curr = curr.parent
            i += 1
        elif ch == ",":
            i += 1
        else:
            sub_s = ""
            while s[i].isdigit():
                sub_s += s[i]
                i += 1
            new_node = Node(parent=curr, value=int(sub_s))
            curr.children.append(new_node)
    return root


def compare_values(x, y):
    if x < y:
        return -1
    elif x == y:
        return 0
    else:
        return 1


def compare(t1, t2):
    # returns -1 if t1 < t2, 0 if t1 == t2, and 1 if t1 > t2
    if (t1.value is not None) and (t2.value is not None):
        return compare_values(t1.value, t2.value)
    elif (t1.value is None) and (t2.value is None):
        for i in range(min(len(t1.children), len(t2.children))):
            if (curr_comp := compare(t1.children[i], t2.children[i])) != 0:
                return curr_comp
        return compare_values(len(t1.children), len(t2.children))
    elif t1.value is not None:
        new_node = Node(parent=t1, value=t1.value)
        t1.value = None
        t1.children = [new_node]
        return compare(t1, t2)
    elif t2.value is not None:
        new_node = Node(parent=t2, value=t2.value)
        t2.value = None
        t2.children = [new_node]
        return compare(t1, t2)


trees = [str_to_tree(s) for s in strings]
sorted_ind = sorted(range(len(trees)), key=cmp_to_key(lambda i, j: compare(trees[i], trees[j])))
print((sorted_ind.index(len(trees) - 1) + 1) * (sorted_ind.index(len(trees) - 2) + 1))
