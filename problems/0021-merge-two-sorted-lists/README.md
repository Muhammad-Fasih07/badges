# 21. Merge Two Sorted Lists

**Difficulty:** Easy
**Status:** Open for contributors

## Problem

You are given the heads of two sorted linked lists. Merge them into one sorted list by reusing the existing nodes, then return the head of the merged list.

## Examples

**Example 1**

```text
Input: list1 = 1 -> 2 -> 4, list2 = 1 -> 3 -> 4
Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4
```

**Example 2**

```text
Input: list1 = empty, list2 = empty
Output: empty
```

**Example 3**

```text
Input: list1 = empty, list2 = 0
Output: 0
```

## Constraints

- Each list has between `0` and `50` nodes
- Node values are between `-100` and `100`
- Both lists are sorted in non-decreasing order

## Hint

Walk both lists and always attach the smaller current node. A dummy head makes the first insert easier.

## Solutions

No solutions yet. Add one:

```text
python/solution.py
javascript/solution.js
java/solution.java
```
