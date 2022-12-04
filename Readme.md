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

