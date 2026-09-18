# 20. Valid Parentheses

**Difficulty:** Easy
**Status:** Example solution available

## Problem

Given a string `s` that contains only `()`, `[]`, and `{}`, decide whether the string is valid.

A string is valid when:

- Every opening bracket has a matching closing bracket of the same type
- Brackets close in the correct order
- Every closing bracket has a matching opening bracket

## Examples

**Example 1**

```text
Input: s = "()"
Output: true
```

**Example 2**

```text
Input: s = "()[]{}"
Output: true
```

**Example 3**

```text
Input: s = "(]"
Output: false
```

**Example 4**

```text
Input: s = "([)]"
Output: false
```

**Example 5**

```text
Input: s = "{[]}"
Output: true
```

## Constraints

- `1 <= s.length <= 10^4`
- `s` contains only `()[]{}`

## Hint

A stack is a good fit: push opening brackets, and pop when a matching closer appears.

## Solutions

- [Python](python/solution.py)
