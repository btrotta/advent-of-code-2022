from utilities import parse_multi_string
import operator
from collections import defaultdict


class Node:

    def __init__(self, val=None, left=None, right=None, op=None):
        self.val = val
        self.left = left
        self.right = right
        self.op = op


nodes = defaultdict(lambda: Node())
arr = parse_multi_string(sep=" ")
op_dict = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}
for a in arr:
    name = a[0].replace(":", "")
    node = nodes[name]
    node.name = name
    if a[1].isdigit():
        node.val = int(a[1])
    else:
        left, op, right = a[1:]
        node.left = nodes[left]
        node.right = nodes[right]
        node.op = op_dict[op]

# traverse the tree
to_visit = [nodes["root"]]
while len(to_visit) > 0:
    node = to_visit[-1]
    if node.val is not None:
        to_visit.pop()
        continue
    if node.left.val is None:
        to_visit.append(node.left)
        continue
    if node.right.val is None:
        to_visit.append(node.right)
        continue
    node.val = node.op(node.left.val, node.right.val)

print(int(nodes["root"].val))
