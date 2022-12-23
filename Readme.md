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

## Day 7
Parse the directory structure into a graph. Traverse the graph depth-first to find the total size of each directory (so that
we visit all the sub-directories and add their sizes to the parent before visiting the parent). 
Note that there are distinct directories (at different places in the directory structure) having the same names!

## Day 8
For part 1, iterate over each row and column in both directions, keeping track of the maximum height seen so far. A 
tree is visible if its height is less than current maximum. Using numpy allows us to manipulate the arrays easily.
For part 2, the most obvious solution has complexity $O(n^3)$ where
$n$ is the number of rows/columns: there are $n^2$ trees, and, for a given tree, we can iterate over the indexes before 
it in the same row/column to find the 
last one having equal or greater height. However, since the set of possible heights is small (there are only 10), we can 
achieve a more efficient $O(n^2)$ solution by using a lookup table to keep track of the last index each height was seen.

## Day 9
For part 1, for each move we can immediately calculate the final position of the head, then calculate the tail's 
trajectory given its current position and the head's new position. For part 2, this approach no longer works, so we need 
to process one step at a time.

## Day 10
Note that in an `addx` instruction, `X` doesn't get updated until _after_ 2 cycles
are complete, so all processing that happens during the 2 cycles (calculating the signal strength in part 1, or 
updating the display in part 2) should happen before `X` is incremented.

## Day 11
For part 1, just simulate the rounds. For part 2, the worry levels become very large and consume a lot of memory. 
We can handle this by instead working with the worry level modulo a certain modulus. 
Note that each monkey's test is whether the worry level is divisible 
by some factor. This will give the same result if we replace the worry level by its modulus modulo `m`, where `m` is 
any multiple of the monkey's factor. Therefore we choose `m` to be the lowest common multiple (LCM) of all the monkeys' 
test factors. Before throwing each item, we replace its worry level by the worry level modulo this LCM.

## Day 12
Convert the array to integer values to make comparing elevations easier. To find the shortest paths, use breadth-first
search.

## Day 13
Represent the nested lists as trees, and use a recursive function to compare them according to the rules.

## Day 14
Represent coordinates as complex numbers. Use a set to keep track of filled positions.

## Day 15
Part 1: Let $s = (s_0, s_1)$ and $b = (b_0, b_1)$ be the coordinates of a given sensor and its closest beacon. The distance 
between them is $d = \textup{abs}(s_0 - b_0) + \textup{abs}(s_1 - b1)$. For a given $y$, a point
$(x, y)$ is closer to $s$ than $b$ if $\textup{abs}(x - s_0) < d - abs(y - s_1)$. So there cannot be any beacons 
in the range $[s_0 - (d - \textup{abs}(y - s_1)), s_0 + (d - \textup{abs}(y - s_1))]$. We need to calculate
the union of all these ranges. We can do this efficiently by ordering the ranges by their left edge.

Part 2: Since we are told there is only one possible location for the unknown beacon, it must be either in one
of the corners of the allowable range, or adjoining a point where 2 empty ranges intersect. We can find these 
intersections using linear algebra.

## Day 16
First, find the shortest paths between all pairs of valves with non-zero flow (and the shortest path between the starting
valve AA and all non-zero flow valves). For part 1, use depth-first search to find the path with length <= 30 having 
the best flow. The "nodes" in the graph to be searched represent the current location (always either the starting valve AA 
or a valve with non-zero flow), the current time, the set of currently-opened valves in the current path, and the total 
flow from currently-opened valves. This search is sped up by pre-calculating shortest distances between non-zero flow valves as 
described above, and be representing the set of opened valves using a binary encoding. For part 2, do a similar depth-first 
search as in part 1, but also keep a record of all sets of open valves checked and their flows. 
Then, iterate over pairs of these sets having empty intersection to find the optimal pair.

## Day 17
For part 1, just run the simulation. For part 2, notice that after some time, the rocks will fill the chamber so that 
it's impossible for any rocks to land below some vertical level. When this happens, we can redefine this level as the 
new floor. If we do this, after running the simulation for some time we see that the state repeats (where state is 
defined as the type of rock falling, the index of the jet pattern, and the location of the currently fallen rocks on 
the floor). Then, since we know what happens during this repeating section, we can loop over this repeating part without
actually simulating each rock fall.

## Day 18
For part 1, for each cube, count how many of the adjoining cubes are in the droplet. For part 2, consider a graph where 
each empty point (i.e. each point not part of the droplet) is a node, and the edges connect adjoining empty points. 
(It suffices to  consider all empty points that are at within 1 unit of the minimum and maximum extent of the droplet in each dimension.) Find 
the connected components of this graph. Then iterate over these components to find the unique component containing a point outside 
the droplet. All other components are interior to the droplet.

## Day 20
Use a doubly-linked list. Note that if the number `n`  of positions to move is greater than the length of the array `arr`, 
we must move `n % (len(arr) - 1)` positions (because each time we move one position, we pass one member of the array, 
so after moving `len(arr) - 1` positions we have passed all other members of the array are back in the original position).

## Day 21
The task is to evaluate an expression given in the form of a binary tree. For part 1, use in-order traversal. For part 2, 
we need to solve an equation where `humn` represents the unknown value. Before traversing the tree, change the value of 
node `humn` to `np.nan`, and during the traversal find the path from `root` to `humn`. Then we can solve the equation 
by reversing the operations in this path.


## Day 23
Simulate the moves, using a set to keep track of elves positions (for faster checking).

