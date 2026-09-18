# Time: O(n) | Space: O(n)
# Hash map stores each number and its index while we scan once.


def two_sum(nums: list[int], target: int) -> list[int]:
    seen: dict[int, int] = {}

    for index, value in enumerate(nums):
        needed = target - value
        if needed in seen:
            return [seen[needed], index]
        seen[value] = index

    raise ValueError("No valid pair exists")
