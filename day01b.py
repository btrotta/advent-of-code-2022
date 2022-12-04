with open("data.txt", "r") as f:
    data = f.readlines()

sums = []
curr_sum = 0
for d in data:
    if d == "\n":
        sums.append(curr_sum)
        curr_sum = 0
    else:
        curr_sum += int(d)

print(sum(sorted(sums)[-3:]))
