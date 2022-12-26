from utilities import parse_single_string
import math

arr = parse_single_string()

to_decimal = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
decimal_ans = 0
for a in arr:
    for i, ch in enumerate(reversed(a)):
        decimal_ans += to_decimal[ch] * 5**i

power = math.floor(math.log(decimal_ans, 5))
base_5_digits = []
while power >= 0:
    base_5_digits.append(decimal_ans // (5 ** power))
    decimal_ans = decimal_ans % (5 ** power)
    power -= 1

carry = 0
for i in range(len(base_5_digits) - 1, -1, -1):
    d = base_5_digits[i] + carry
    base_5_digits[i] = d % 5
    carry = d // 5
    if d == 3:
        base_5_digits[i] = -2
        carry = 1
    elif d == 4:
        base_5_digits[i] = -1
        carry = 1
if carry > 0:
    base_5_digits = [carry] + base_5_digits


to_snafu = {0: "0", 1: "1", 2: "2", -2: "=", -1: "-"}
ans = "".join(to_snafu[d] for d in base_5_digits)

print(ans)
