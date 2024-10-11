# Advent of Code 2023

## Day 1

### [Part 1](day1a.py)

We retain all numeric characters, and compute the resulting number for each line.

### [Part 2](day1b.py)

Using the [KMP](https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm) algorithm, we get all
occurrences of all alphabetic digits, and combine this with the numeric digits. We then sort by index of first
occurrence, and compute the resulting number from the first and last digit on each line.

## Day 2

### Part 1

### Part 2
