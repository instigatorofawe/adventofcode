# Advent of Code 2023

## Day 1

### [Part 1](day1a.py)

We retain all numeric characters, and compute the resulting number for each line.

### [Part 2](day1b.py)

Using the [KMP](https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm) algorithm, we get all
occurrences of all alphabetic digits, and combine this with the numeric digits. We then sort by index of first
occurrence, and compute the resulting number from the first and last digit on each line.

## Day 2

### [Part 1](day2a.py)

A simple parsing exercise, using string split and list comprehensions.

### [Part 2](day2b.py)

A simple follow-up; we compute the maximum number of balls of each color for each line using a Dict to store values.

## Day 3

### [Part 1](day3a.py)

We compute all the start and end indices of numbers on each row, as well as the indices of symbols on each row. For each
number, we then look for an adjacent symbol, searching the three adjacent rows.

### [Part 2](day3b.py)

Similar to the previous part, except each asterisk's row and column are indexed in a Dict, which maps to a list of all
numbers. We compute the product for all lists with two elements.

## Day 4

### [Part 1](day4a.py)

We parse the scratch cards, and compute the number of matches for each row. If there are no matches, the row scores 0
points, otherwise it scores 2^(matches - 1).

### [Part 2](day4b.py)

We use dynamic programming, where if a card has 0 matches, then it contributes only 1 card. Otherwise, it contributes 1
and the sum of the next m cards.

## Day 5

### [Part 1](day5a.py)

We simply store a sorted list of non-overlapping segments. For each value we wish to map, we see if it is contained
within a segment, and add the corresponding offset. We do this for all 7 mappings.

### [Part 2](day5b.py)

Instead of individual values, we have to compute mappings for segments. We do this by checking if there are any
intersections between the segment we wish to map, and the ranges in the mapping. We add the corresponding offset to all
overlapping segments.

## Day 6

### [Part 1](day6a.py)

We can simply iterate through the range and compute if we can equal the record for each race.

### [Part 2](day6b.py)

We can use binary search to find the start and end of the viable range.

## Day 7

### [Part 1](day7a.py)

We keep a dictionary of the counts of each rank in the hand. We then convert the counts to a tuple sorted in decreasing
order. We sort by this tuple, and then sort by the ranks of each card in the hand. The individual ranks, however, are
not sorted.

### [Part 2](day7b.py)

We count the number of jokers and increase the multiplicity of the highest multiplicity rank by that number.

## Day 8

### [Part 1](day8a.py)

We simply build the map and follow the instructinos until we reach ZZZ.

### [Part 2](day8b.py)

Starting from each node that ends with A, we count the number of steps until we end up with a node that ends with Z. We
then compute the least common multiple of all of these.

## Day 9

### [Part 1](day9a.py)

As the examples suggest, we build a stack of lists of differences until we end up with all 0s. We then pop each layer,
adding the last value to the last value of the next layer until we reach the bottom.

### [Part 2](day9b.py)

We do this at the beginning, except we subtract the first value of the layer we popped from the first value of the next
layer.

## Day 10

### [Part 1](day10a.py)

Beginning at S, we check the neighbors to see which shapes are viable candidates. For each candidate, we then follow the
pipes until we hit an invalid connection or we make a full loop, counting the number of segments in the loop. The
maximum distance is equal to half the number of segments.

### [Part 2](day10b.py)

We compute a new map, where we only have empty space and the pipe segments within the loop. We then traverse from left
to right, keeping track of the number of boundaries we have crossed. If the number of boundaries is odd, we are within
the enclosed area.

## Day 11

### [Part 1](day11a.py)

We simply compute the pairwise manhattan distance betwen each set of stars. We keep track of the indices of empty rows
and columns, and add 1 for each empty row or column we must cross.

### [Part 2](day11b.py)

Same as Part 1, but we add 999 for each empty row or column we must cross.


