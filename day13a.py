with open("data.txt", "r") as f:
    data = f.readlines()

pairs = []
for i in range(0, len(data), 3):
    pairs.append([data[i].replace("\n", ""), data[i + 1].replace("\n", "")])


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


ans = 0
for ind, (p1, p2) in enumerate(pairs):
    t1 = str_to_tree(p1)
    t2 = str_to_tree(p2)
    if compare(t1, t2) < 0:
        ans += ind + 1
print(ans)
