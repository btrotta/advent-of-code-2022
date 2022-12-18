from utilities import parse_multi_string
from copy import deepcopy

arr = parse_multi_string(sep=" ")


class Valve:

    def __init__(self, name, flow, neighbours=None, is_open=False):
        self.name = name
        self.flow = flow
        self.neighbours = neighbours
        self.is_open = is_open


valves = {}
for a in arr:
    name = a[1]
    flow = int(a[4][5:-1])
    neighbours = [x.replace(",", "") for x in a[9:]]
    valves[name] = Valve(name, flow, neighbours)

# duplicate set of valves to represent opening valve
valves_to_open = {}
for name, v in valves.items():
    if v.flow > 0:
        new_name = name + "_open"
        new_valve = Valve(new_name, v.flow, v.neighbours, True)
        v.flow = 0
        valves_to_open[new_name] = new_valve
        v.neighbours = v.neighbours + [new_name]
valves.update(valves_to_open)

# keys of best are the valves that can be reached by time t
# best[v] = (best_flow, open_valves) where best_flow is the optimal flow that can be
# obtained by a path ending at valve v at time t, and open_valves is the set of valves
# opened to obtain that flow
best = {"AA": (0, set())}
for t in range(1, 30):
    new_best = deepcopy(best)
    for v_name in best:
        v = valves[v_name]
        best_flow_v, open_valves = best[v_name]
        if len(open_valves) == len(valves_to_open):
            continue
        for n_name in v.neighbours:
            n = valves[n_name]
            if (n_name in open_valves) and n.is_open:
                continue
            new_total_flow = best_flow_v + n.flow * (30 - t)
            new_open_valves = open_valves.union({n_name}) if n.is_open else open_valves
            best_flow_n = new_best.get(n_name, (-1, set()))[0]
            if new_total_flow > best_flow_n:
                new_best[n_name] = new_total_flow, new_open_valves
    best = new_best

print(max(best.values())[0])
