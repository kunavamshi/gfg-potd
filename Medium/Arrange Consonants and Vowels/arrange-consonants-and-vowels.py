"""
# Node Class
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
"""

class Solution:
    # Function to arrange vowels before consonants while maintaining order.
    def arrangeCV(self, head):
        if not head or not head.next:
            return head
        
        # Helper functions to check if a character is a vowel or a consonant.
        def isVowel(char):
            return char in ['a', 'e', 'i', 'o', 'u']
        
        def isConsonant(char):
            return char.isalpha() and not isVowel(char)
        
        # Separate vowels and consonants into two separate lists.
        vowel_head = Node(None)
        consonant_head = Node(None)
        vowel_tail = vowel_head
        consonant_tail = consonant_head
        
        current = head
        while current:
            if isVowel(current.data):
                vowel_tail.next = current
                vowel_tail = current
            else:
                consonant_tail.next = current
                consonant_tail = current
            current = current.next
        
        # Merge the two lists while preserving order.
        vowel_tail.next = consonant_head.next
        consonant_tail.next = None
        
        return vowel_head.next

#{ 
 # Driver Code Starts
# Node Class
class Node:

    def __init__(self, val):
        self.data = val
        self.next = None


# Linked List Class
class Linked_List:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next


def printList(head):
    tmp = head
    while tmp:
        print(tmp.data, end=' ')
        tmp = tmp.next
    print()


if __name__ == '__main__':
    for i in range(int(input())):
        n = int(input())
        arr = [str(x) for x in input().split()]

        lis = Linked_List()
        for i in arr:
            lis.insert(i)

        newHead = Solution().arrangeCV(lis.head)
        printList(newHead)

# } Driver Code Ends