# two pointers
class Solution:
    def hasCycle(self, head:ListNode) -> bool:
        fast = head
        slow = head # start the fast and slow at the same position, the next time they meet each other is the time we know we've detect a loop
        while fast and fast.next: # is not null # also need to include fast.next beacuse we are shifting fast by two on each iteration
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
    
  #hash table
class Solution:
    def hasCycle(self, head:ListNode) -> bool:
        seen = set()
        cur = head
        while cur: # is not null
            if cur in seen:
                return True
            seen.add(cur)
            cur = cur.next
        return False
