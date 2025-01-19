class Solution:
    # Function to rotate a linked list.
    def rotate(self, head, k):
        if not head or not head.next or k == 0:
            return head

        # Compute the length of the linked list
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # Optimize k to avoid unnecessary rotations
        k = k % length
        if k == 0:
            return head

        # Find the new head and break the list
        current = head
        for _ in range(k - 1):
            current = current.next

        new_head = current.next
        current.next = None
        tail.next = head  # Connect the old tail to the old head

        return new_head

#{ 
 # Driver Code Starts
#Initial Template for Python 3


# Define the Node class for the linked list
class Node:

    def __init__(self, x):
        self.data = x
        self.next = None


# Function to print the linked list
def printList(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()


#Position this line where user code will be pasted.

# Main function
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    t = int(data[0].strip())
    idx = 1

    while t > 0:
        arr = list(map(int, data[idx].strip().split()))

        head = None
        if arr:
            head = Node(arr[0])
            tail = head
            for num in arr[1:]:
                tail.next = Node(num)
                tail = tail.next

        k = int(data[idx + 1].strip())
        idx += 2
        head = Solution().rotate(head, k)
        printList(head)
        print("~")
        t -= 1

# } Driver Code Ends