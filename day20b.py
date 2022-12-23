from utilities import parse_single_int

arr = parse_single_int()
key = 811589153
arr = [a * key for a in arr]
move_arr = [a % (len(arr) - 1) for a in arr]


class Node:

    def __init__(self, val, move):
        self.val = val
        self.move = move
        self.prev = None
        self.next = None


node_list = [Node(val, move) for val, move in zip(arr, move_arr)]
for i in range(len(arr)):
    node = node_list[i]
    if i > 0:
        node.prev = node_list[i - 1]
    if i < len(arr) - 1:
        node.next = node_list[i + 1]
node_list[0].prev = node_list[-1]
node_list[-1].next = node_list[0]

for mix in range(10):
    for node in node_list:
        move = node.move
        if move == 0:
            continue
        move = move % (len(arr) - 1)
        if move > 0:
            curr = node
            for i in range(move):
                new_prev = curr.next
                curr = curr.next
        elif move < 0:
            curr = node
            for i in range(-move + 1):
                new_prev = curr.prev
                curr = curr.prev
        new_next = new_prev.next
        old_prev = node.prev
        old_next = node.next
        node.prev = new_prev
        node.next = new_next
        new_prev.next = node
        new_next.prev = node
        old_prev.next = old_next
        old_next.prev = old_prev

# find 0
for node in node_list:
    if node.val == 0:
        break
ans = 0
for i in range(3001):
    if i in [1000, 2000, 3000]:
        ans += node.val
    node = node.next

print(ans)
