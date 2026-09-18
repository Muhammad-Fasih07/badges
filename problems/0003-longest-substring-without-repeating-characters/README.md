# 3. Longest Substring Without Repeating Characters

**Difficulty:** Medium
**Status:** Open for contributors

## Problem

Given a string `s`, return the length of the longest substring that contains no repeated characters.

A substring is a contiguous piece of the string.

## Examples

**Example 1**

```text
Input: s = "abcabcbb"
Output: 3
Explanation: "abc"
```

**Example 2**

```text
Input: s = "bbbbb"
Output: 1
Explanation: "b"
```

**Example 3**

```text
Input: s = "pwwkew"
Output: 3
Explanation: "wke"
```

## Constraints

- `0 <= s.length <= 5 * 10^4`
- `s` may contain English letters, digits, symbols, and spaces

## Hint

Use a sliding window. Move the right pointer forward, and move the left pointer when a duplicate enters the window.

## Solutions

No solutions yet. Add one:

```text
python/solution.py
javascript/solution.js
java/solution.java
```
