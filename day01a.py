with open("data.txt", "r") as f:
    data = f.readlines()

curr_max = 0
curr_sum = 0
for d in data:
    if d == "\n":
        curr_max = max(curr_sum, curr_max)
        curr_sum = 0
    else:
        curr_sum += int(d)

print(curr_max)
