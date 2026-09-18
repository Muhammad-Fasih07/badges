# 70. Climbing Stairs

**Difficulty:** Easy
**Status:** Example solution available

## Problem

You are climbing a staircase with `n` steps. Each move you may take either `1` step or `2` steps. Return how many distinct ways you can reach the top.

## Examples

**Example 1**

```text
Input: n = 2
Output: 2
Explanation: 1+1 and 2
```

**Example 2**

```text
Input: n = 3
Output: 3
Explanation: 1+1+1, 1+2, and 2+1
```

## Constraints

- `1 <= n <= 45`

## Hint

The number of ways to reach step `n` is the sum of the ways to reach `n-1` and `n-2`.

## Solutions

- [Python](python/solution.py)
