# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find middle point of list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # breaks with second half being at slow.next, and set end of first list to None (break connection)
        second = slow.next
        slow.next = None

        # Reverse second half of list
        curr, prev = second, None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # after reversing, head of reversed list is prev
        second = prev
        first = head

        # Merge two halfs, one starting at head, ,
        while second:  # guaranteed shorter
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1  # insert second between first and first.next

            first, second = tmp1, tmp2