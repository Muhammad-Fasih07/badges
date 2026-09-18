# 704. Binary Search

**Difficulty:** Easy
**Status:** Open for contributors

## Problem

Given a sorted array `nums` in ascending order and a target value, return the index of `target` if it exists. If it does not exist, return `-1`.

Your algorithm should run in `O(log n)` time.

## Examples

**Example 1**

```text
Input: nums = [-1, 0, 3, 5, 9, 12], target = 9
Output: 4
```

**Example 2**

```text
Input: nums = [-1, 0, 3, 5, 9, 12], target = 2
Output: -1
```

## Constraints

- `1 <= nums.length <= 10^4`
- `-10^4 <= nums[i], target <= 10^4`
- All values in `nums` are unique
- `nums` is sorted in ascending order

## Hint

Keep a left and right bound. Compare the middle value with the target and throw away half of the remaining range each step.

## Solutions

No solutions yet. Add one:

```text
python/solution.py
javascript/solution.js
java/solution.java
```
