# Advent of Code 2023

## Day 1

### [Part 1](day1a.rs)

Same approach as Python; for each line, we filter for numeric digits.

### [Part 2](day1b.rs)

Also same approach as Python; we use KMP algorithm to compute all substring matches, combine tuples of indices and digit
values, sort the resulting array, then compute the final value.
