from utilities import *
from collections import deque

arr = parse_single_string()


class Monkey:
    def __init__(self):
        self.items = deque()
        self.op = None
        self.factor = 1
        self.if_true = -1
        self.if_false = -1
        self.num_inspections = 0

    def test(self, x):
        return x % self.factor == 0


monkeys = []
for a in arr:
    a = a.strip()
    if a.startswith("Monkey"):
        monkeys.append(Monkey())
    elif a.startswith("Starting"):
        items = [int(x) for x in a.split(": ")[1].split(", ")]
        monkeys[-1].items = deque(items)
    elif a.startswith("Operation"):
        op = a.split(": ")[1].split(" =")[1]
        monkeys[-1].op = eval(f"lambda old: {op}")
    elif a.startswith("Test"):
        monkeys[-1].factor = int(a.split(" ")[-1])
    elif a.startswith("If true"):
        monkeys[-1].if_true = int(a.split(" ")[-1])
    elif a.startswith("If false"):
        monkeys[-1].if_false = int(a.split(" ")[-1])


for r in range(20):
    for m in monkeys:
        while len(m.items) > 0:
            item = m.items.popleft()
            wl = m.op(item)
            wl = wl // 3
            throw_to = m.if_true if m.test(wl) else m.if_false
            monkeys[throw_to].items.append(wl)
            m.num_inspections += 1

num_inspections = sorted([m.num_inspections for m in monkeys])
print(num_inspections[-1] * num_inspections[-2])


