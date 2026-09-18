# 206. Reverse Linked List

**Difficulty:** Easy
**Status:** Example solution available

## Problem

Reverse a singly linked list and return the new head.

Each node has a `val` and a `next` pointer.

## Examples

**Example 1**

```text
Input: 1 -> 2 -> 3 -> 4 -> 5
Output: 5 -> 4 -> 3 -> 2 -> 1
```

**Example 2**

```text
Input: 1 -> 2
Output: 2 -> 1
```

**Example 3**

```text
Input: empty list
Output: empty list
```

## Constraints

- The list has between `0` and `5000` nodes
- Node values are between `-5000` and `5000`

## Hint

Keep three pointers: previous, current, and next. Walk the list and reverse one link at a time.

## Solutions

- [Python](python/solution.py)
