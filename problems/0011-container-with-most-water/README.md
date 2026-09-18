# 11. Container With Most Water

**Difficulty:** Medium
**Status:** Open for contributors

## Problem

You are given an array `height` of length `n`. There are `n` vertical lines, and the `i`-th line has height `height[i]`.

Choose two lines that, together with the x-axis, form a container. Return the maximum amount of water the container can store.

Water cannot be slanted. The width is the distance between the two chosen indices.

## Examples

**Example 1**

```text
Input: height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
Output: 49
Explanation: The lines at index 1 and index 8 form the largest container.
```

**Example 2**

```text
Input: height = [1, 1]
Output: 1
```

## Constraints

- `2 <= height.length <= 10^5`
- `0 <= height[i] <= 10^4`

## Hint

Start with the widest pair of lines. Move the pointer at the shorter line inward, because that is the only move that can increase the area.

## Solutions

No solutions yet. Add one:

```text
python/solution.py
javascript/solution.js
java/solution.java
```
