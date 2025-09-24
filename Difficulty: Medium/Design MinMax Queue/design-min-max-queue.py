from collections import deque

class SpecialQueue:
    def __init__(self):
        self.q = deque()        # Normal queue
        self.minq = deque()     # Monotonic increasing (for min)
        self.maxq = deque()     # Monotonic decreasing (for max)

    def enqueue(self, x):
        self.q.append(x)

        # Maintain min queue (increasing order)
        while self.minq and self.minq[-1] > x:
            self.minq.pop()
        self.minq.append(x)

        # Maintain max queue (decreasing order)
        while self.maxq and self.maxq[-1] < x:
            self.maxq.pop()
        self.maxq.append(x)

    def dequeue(self):
        if self.q:
            val = self.q.popleft()
            if self.minq and self.minq[0] == val:
                self.minq.popleft()
            if self.maxq and self.maxq[0] == val:
                self.maxq.popleft()

    def getFront(self):
        return self.q[0] if self.q else -1

    def getMin(self):
        return self.minq[0] if self.minq else -1

    def getMax(self):
        return self.maxq[0] if self.maxq else -1