# Python solutions for Advent of Code 2022

## Day 1
For part 1, iterate over the arrays and keep track of the current maximum calorie total. For part 2, build an array
of all elves' calorie totals, then sort it and sum the last 3 values.

## Day 2
For part 1, use dictionaries to look up the score. For part 2, notice that if we represent each player's choice as
either 0, 1, or 2 (representing Rock, Paper, Scissors), and label players' choices as ind1 and ind2, then player 2 wins
whenever `(ind2 - 1) % 3 == ind1`. This simplifies the calculation of scores and strategies.

## Day 3
Convert the strings to lists and use `np.intersect1d` to find the intersection.

## Day 4
For part 1, `(a, b)` contains `(x, y)` if `a <= x` and `b >= y`. For part 2, 
`(a, b)` and `(x, y)` intersect if `max(a, x) <= min(b, y)`.

## Day 5
Represent the cargo stacks as lists. For part 1, use `pop` to move the top items one by one. For part 2, 
remove the items as a block.

## Day 6
For part 1, iterate over the string, starting at position 4. Get the last 4 characters, convert to a set, and check
whether the length of the set is equal to 4. Part 2 is similar, except using 14 characters.

