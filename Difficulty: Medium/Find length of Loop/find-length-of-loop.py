class Solution:
    def lengthOfLoop(self, head):
        if not head or not head.next:
            return 0
        
        slow = head
        fast = head
        
        # Step 1: Detect loop
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:  # loop detected
                # Step 2: Count loop length
                count = 1
                temp = slow.next
                while temp != slow:
                    count += 1
                    temp = temp.next
                return count
        
        return 0  # no loop