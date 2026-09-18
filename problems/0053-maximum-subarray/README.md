# 53. Maximum Subarray

**Difficulty:** Easy
**Status:** Open for contributors

## Problem

Given an integer array `nums`, find the contiguous subarray with the largest sum and return that sum.

A subarray is a sequence of one or more items that sit next to each other in the array.

## Examples

**Example 1**

```text
Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
Explanation: [4, -1, 2, 1] has the largest sum.
```

**Example 2**

```text
Input: nums = [1]
Output: 1
```

**Example 3**

```text
Input: nums = [5, 4, -1, 7, 8]
Output: 23
```

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

## Hint

Kadane's algorithm keeps a running sum and resets it when that running sum becomes worse than starting over.

## Solutions

No solutions yet. Add one:

```text
python/solution.py
javascript/solution.js
java/solution.java
```
