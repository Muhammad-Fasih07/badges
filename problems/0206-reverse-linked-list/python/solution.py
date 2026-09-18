# Time: O(n) | Space: O(1)
# Reverse each pointer while walking the list once.


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


def reverse_list(head: ListNode | None) -> ListNode | None:
    previous = None
    current = head

    while current is not None:
        nxt = current.next
        current.next = previous
        previous = current
        current = nxt

    return previous
