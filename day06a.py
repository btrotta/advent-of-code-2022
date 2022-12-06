from utilities import *

chars = parse_single_string()[0]

for i in range(4, len(chars)):
    if len(set(chars[i-4:i])) == 4:
        break

print(i)
