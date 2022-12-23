from utilities import parse_multi_string
import operator
from collections import defaultdict
import numpy as np


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

# traverse the tree to find path from root to humn
# all unknown values will be set to np.nan during the traversal
nodes["humn"].val = np.nan
path = [nodes["root"]]
to_visit = [nodes["root"]]
while len(to_visit) > 0:
    node = to_visit[-1]
    if node.val is not None:
        path.pop()
        to_visit.pop()
        continue
    if node.left.val is None:
        to_visit.append(node.left)
        path.append(node.left)
        continue
    if node.right.val is None:
        to_visit.append(node.right)
        path.append(node.right)
        continue
    node.val = node.op(node.left.val, node.right.val)
    if node.left.name == "humn" or node.right.name == "humn":
        path_to_humn = [p for p in path]

# reverse the operations in the path to find the unknown value
node = nodes["root"]
target_val = node.right.val if np.isnan(node.left.val) else node.left.val
for i, node in enumerate(path_to_humn[1:]):
    if np.isnan(node.left.val):
        val = node.right.val
        unknown_on_left = True
    else:
        val = node.left.val
        unknown_on_left = False
    if node.op == operator.add:
        target_val -= val
    elif node.op == operator.mul:
        target_val /= val
    elif node.op == operator.truediv:
        if unknown_on_left:
            target_val *= val
        else:
            target_val = val / target_val
    elif node.op == operator.sub:
        if unknown_on_left:
            target_val += val
        else:
            target_val = val - target_val

print(int(target_val))
