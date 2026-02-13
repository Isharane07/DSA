class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        temp = dummy
        carry = 0

        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next

            if l2:
                carry += l2.val
                l2 = l2.next

            temp.next = ListNode(carry % 10)
            carry //= 10
            temp = temp.next

        return dummy.next
