# two pointers
class Solution:
    def hasCycle(self, head:ListNode) -> bool:
        fast = head
        slow = head
        while fast and fast.next: # is not null
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
