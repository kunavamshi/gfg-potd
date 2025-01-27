from collections import OrderedDict

class LRUCache:
    # Constructor for initializing the cache capacity with the given value.
    def __init__(self, cap):
        self.capacity = cap
        self.cache = OrderedDict()  # Maintains the order of key insertion

    # Function to return value corresponding to the key.
    def get(self, key):
        if key in self.cache:
            self.cache.move_to_end(key)  # Mark as recently used
            return self.cache[key]
        return -1

    # Function for storing key-value pair.
    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)  # Mark as recently used
        elif len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)  # Remove least recently used item
        self.cache[key] = value  # Insert new key-value pair




#{ 
 # Driver Code Starts
#Initial Template for Python 3


def inputLine():
    return input().strip().split()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        capacity = int(input())
        cache = LRUCache(capacity)

        queries = int(input())
        for __ in range(queries):
            vec = inputLine()
            if vec[0] == "PUT":
                key = int(vec[1])
                value = int(vec[2])
                cache.put(key, value)
            else:
                key = int(vec[1])
                print(cache.get(key), end=" ")
        print()
        print("~")

# } Driver Code Ends