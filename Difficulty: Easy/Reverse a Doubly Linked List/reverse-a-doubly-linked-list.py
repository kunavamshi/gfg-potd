class Solution:
    def reverse(self, head):
        if not head:
            return None
        
        curr = head
        prev_node = None
        
        while curr:
            # swap next and prev
            curr.prev, curr.next = curr.next, curr.prev
            prev_node = curr
            curr = curr.prev   # move to original next (since swapped)
        
        return prev_node   # new head