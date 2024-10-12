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
