# 49. Group Anagrams

**Difficulty:** Medium
**Status:** Open for contributors

## Problem

Given an array of strings `strs`, group the anagrams together. Anagrams are words that use the same letters with the same counts.

Return the groups in any order. The order of words inside a group also does not matter.

## Examples

**Example 1**

```text
Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
```

**Example 2**

```text
Input: strs = [""]
Output: [[""]]
```

**Example 3**

```text
Input: strs = ["a"]
Output: [["a"]]
```

## Constraints

- `1 <= strs.length <= 10^4`
- `0 <= strs[i].length <= 100`
- `strs[i]` contains lowercase English letters

## Hint

Use a map whose key is a sorted version of the word, or a count of its 26 letters.

## Solutions

No solutions yet. Add one:

```text
python/solution.py
javascript/solution.js
java/solution.java
```
