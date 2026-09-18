# Time: O(n) | Space: O(1)
# Fibonacci-style walk: ways(n) = ways(n-1) + ways(n-2).


def climb_stairs(n: int) -> int:
    if n <= 2:
        return n

    one_before = 2
    two_before = 1

    for _ in range(3, n + 1):
        current = one_before + two_before
        two_before = one_before
        one_before = current

    return one_before
