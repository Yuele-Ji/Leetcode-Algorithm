#hash table
# approach: we can just go through each node one by one, and store the node in hashset, if we have seen a same node we have visit before
#           then there is a cycle in the linked list
class Solution:
    def hasCycle(self, head:ListNode) -> bool:
        nodes_seen = set() # create a set named nodes_seen
        cur = head # set our current node to be head
        while cur: # we will check if the node is seen before while the node is not reaching to the end of the linked list
            if cur in seen: # check if we have already seen the node
                return True # if so, we will return True
            seen.add(cur) # otherwise, let's add this node to the seen set
            cur = cur.next # move our current pointer to the next
        return False
# time complexity: O(n) n is the number of nodes
# space conplexity: O(n)

# reduce the space conplexity to O(1)

# two pointers
class Solution:
def hasCycle(self, head:ListNode) -> bool:
    fast = head
    slow = head # start the fast and slow at the same position
    while fast and fast.next: # we are going to shifting our fast and slow pointers while fast and fast dot next is not null
                              # the reason why we also need to include fast.next beacuse we are shifting fast by two on each iteration
                              # and fast is going to reach the end of the linked list before the slow does that
        fast = fast.next.next # on the inside, we are gonna to check if there is a cycle
        slow = slow.next # take the slow pointer shifted by one 
        if fast == slow: # now if thet meet each other, means slow equals fast, 
            return True # then we can return true
    return False             # so if it does that, then outside the loop we can return false, meaning there does not exist a cycle
#[A,B,C,D,E]
#.    C
# fast slow
# C.   B
