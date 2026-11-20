# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0

        # iterate while either has digits, check for carry, and add 1
        while l1 or l2 or carry:

            sum = 0

            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            new_digit = val1 + val2 + carry
            carry = new_digit // 10
            new_digit = new_digit % 10

            # add to list
            node = ListNode(val=new_digit)
            curr.next = node

            # update
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next