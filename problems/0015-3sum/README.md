# 15. 3Sum

**Difficulty:** Medium
**Status:** Open for contributors

## Problem

Given an integer array `nums`, return all unique triplets `[nums[a], nums[b], nums[c]]` such that:

- `a`, `b`, and `c` are different indices
- `nums[a] + nums[b] + nums[c] == 0`

The result must not contain duplicate triplets. The order of triplets does not matter.

## Examples

**Example 1**

```text
Input: nums = [-1, 0, 1, 2, -1, -4]
Output: [[-1, -1, 2], [-1, 0, 1]]
```

**Example 2**

```text
Input: nums = [0, 1, 1]
Output: []
```

**Example 3**

```text
Input: nums = [0, 0, 0]
Output: [[0, 0, 0]]
```

## Constraints

- `3 <= nums.length <= 3000`
- `-10^5 <= nums[i] <= 10^5`

## Hint

Sort the array first. Fix one number, then use two pointers to find a pair that sums to the opposite value. Skip duplicates as you go.

## Solutions

No solutions yet. Add one:

```text
python/solution.py
javascript/solution.js
java/solution.java
```
