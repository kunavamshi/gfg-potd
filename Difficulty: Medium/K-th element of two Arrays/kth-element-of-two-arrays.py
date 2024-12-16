class Solution:
    def kthElement(self, a, b, k):
        # Two pointer approach to find the k-th element
        i, j, count = 0, 0, 0

        while i < len(a) and j < len(b):
            # Increment count as we compare and move pointers
            if a[i] < b[j]:
                count += 1
                if count == k:
                    return a[i]
                i += 1
            else:
                count += 1
                if count == k:
                    return b[j]
                j += 1

        # Handle remaining elements in array `a`
        while i < len(a):
            count += 1
            if count == k:
                return a[i]
            i += 1

        # Handle remaining elements in array `b`
        while j < len(b):
            count += 1
            if count == k:
                return b[j]
            j += 1

        return -1  # In case k is out of bounds (shouldn't happen with valid input)



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):

        k = int(input())
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.kthElement(a, b, k))
        print("~")
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends