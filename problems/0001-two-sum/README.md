# 1. Two Sum

**Difficulty:** Easy
**Status:** Example solution available

## Problem

You are given an array of integers `nums` and an integer `target`. Return the indices of the two numbers that add up to `target`.

Assume exactly one valid pair exists, and you may not use the same element twice. The order of the two indices does not matter.

## Examples

**Example 1**

```text
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: 2 + 7 = 9
```

**Example 2**

```text
Input: nums = [3, 2, 4], target = 6
Output: [1, 2]
```

**Example 3**

```text
Input: nums = [3, 3], target = 6
Output: [0, 1]
```

## Constraints

- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- Exactly one valid pair exists

## Hint

A hash map can remember numbers you have already seen and the index where each one appeared.

## Solutions

- [Python](python/solution.py)
- [JavaScript](javascript/solution.js)
