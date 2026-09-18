# 121. Best Time to Buy and Sell Stock

**Difficulty:** Easy
**Status:** Example solution available

## Problem

You are given an array `prices` where `prices[i]` is the price of a stock on day `i`.

You may buy on one day and sell on a later day. Return the maximum profit you can earn. If no profit is possible, return `0`.

You may complete at most one transaction.

## Examples

**Example 1**

```text
Input: prices = [7, 1, 5, 3, 6, 4]
Output: 5
Explanation: Buy at 1 and sell at 6.
```

**Example 2**

```text
Input: prices = [7, 6, 4, 3, 1]
Output: 0
Explanation: Prices only go down, so there is no profitable sale.
```

## Constraints

- `1 <= prices.length <= 10^5`
- `0 <= prices[i] <= 10^4`

## Hint

Track the lowest price seen so far, and update the best profit at each later day.

## Solutions

- [Python](python/solution.py)
