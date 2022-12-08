from utilities import parse_single_string

chars = parse_single_string()[0]

for i in range(14, len(chars)):
    if len(set(chars[i-14:i])) == 14:
        break

print(i)
