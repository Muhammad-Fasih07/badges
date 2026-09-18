# 2. Add Two Numbers

**Difficulty:** Medium
**Status:** Open for contributors

## Problem

Two non-empty linked lists represent two non-negative integers. Digits are stored in reverse order, and each node holds one digit.

Add the two numbers and return the sum as a linked list in the same reverse-digit format.

You may assume the two numbers do not contain leading zeros, except for the number `0` itself.

## Examples

**Example 1**

```text
Input: l1 = 2 -> 4 -> 3, l2 = 5 -> 6 -> 4
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807
```

**Example 2**

```text
Input: l1 = 0, l2 = 0
Output: 0
```

**Example 3**

```text
Input: l1 = 9 -> 9 -> 9 -> 9 -> 9 -> 9 -> 9, l2 = 9 -> 9 -> 9 -> 9
Output: 8 -> 9 -> 9 -> 9 -> 0 -> 0 -> 0 -> 1
```

## Constraints

- Each list has between `1` and `100` nodes
- Node values are digits from `0` to `9`

## Hint

Walk both lists at the same time and keep a carry, just like adding numbers on paper.

## Solutions

No solutions yet. Add one:

```text
python/solution.py
javascript/solution.js
java/solution.java
```
