class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        n = len(arr)
        if n == 0:
            return []

        # Initialize two potential candidates and their counts
        candidate1, candidate2, count1, count2 = None, None, 0, 0

        # Phase 1: Identify potential candidates
        for num in arr:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1

        # Phase 2: Confirm the candidates
        result = []
        count1 = count2 = 0
        for num in arr:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1

        if count1 > n // 3:
            result.append(candidate1)
        if count2 > n // 3:
            result.append(candidate2)

        # Return the result in sorted order
        return sorted(result)



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        nums = list(map(int, s.split()))
        ob = Solution()
        ans = ob.findMajority(nums)
        if not ans:
            print("[]")
        else:
            print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()

# } Driver Code Ends