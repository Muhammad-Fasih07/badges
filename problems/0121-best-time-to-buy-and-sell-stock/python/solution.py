# Time: O(n) | Space: O(1)
# Keep the cheapest buy so far and the best profit seen so far.


def max_profit(prices: list[int]) -> int:
    lowest = prices[0]
    best = 0

    for price in prices[1:]:
        best = max(best, price - lowest)
        lowest = min(lowest, price)

    return best
