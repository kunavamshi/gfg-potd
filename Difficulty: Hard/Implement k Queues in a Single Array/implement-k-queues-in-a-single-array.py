class kQueues:

    def __init__(self, n, k):
        self.n = n
        self.k = k
        
        self.arr = [0] * n          # Store actual values
        self.front = [-1] * k       # Front indices of k queues
        self.rear = [-1] * k        # Rear indices of k queues
        self.next = list(range(1, n)) + [-1]  # Free list
        
        self.free = 0               # Start of free list

    def isFull(self):
        return self.free == -1

    def isEmpty(self, i):
        return self.front[i] == -1

    def enqueue(self, x, i):
        if self.isFull():
            return
        
        insert_at = self.free               # Get free index
        self.free = self.next[insert_at]    # Update free
        
        if self.front[i] == -1:             # First element
            self.front[i] = insert_at
        else:
            self.next[self.rear[i]] = insert_at
        
        self.next[insert_at] = -1
        self.rear[i] = insert_at
        self.arr[insert_at] = x

    def dequeue(self, i):
        if self.isEmpty(i):
            return -1
        
        remove_at = self.front[i]
        self.front[i] = self.next[remove_at]
        
        if self.front[i] == -1:
            self.rear[i] = -1
        
        self.next[remove_at] = self.free
        self.free = remove_at
        
        return self.arr[remove_at]