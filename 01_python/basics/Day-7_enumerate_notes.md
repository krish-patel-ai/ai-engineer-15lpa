# enumerate in Python

## What is enumerate?
enumerate is used when we need both the index and the value while looping over a list.

## Why enumerate is useful
It avoids manual counters and reduces bugs.
Python automatically keeps track of the index.

## Simple example
items = ["a", "b", "c"]

for idx, value in enumerate(items):
    print(idx, value)

## Why used in ML / data code
Feature indices must remain consistent.
enumerate preserves original positions when building mappings.

## Interview point
Use enumerate when both index and value are required in a loop.