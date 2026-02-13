class Solution:
    def addTwoNumbers(self, l1, l2):
        c = 0
        h = t = ListNode(0)
        while l1 or l2 or c:
            c += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            t.next = ListNode(c % 10)
            t, c = t.next, c // 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return h.next
