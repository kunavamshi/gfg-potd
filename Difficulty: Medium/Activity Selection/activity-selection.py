class Solution:
    def activitySelection(self, start, finish):
        # Pair start and finish times
        activities = sorted(zip(start, finish), key=lambda x: x[1])

        count = 0
        last_finish = -1  # Tracks the finish time of the last selected activity

        for s, f in activities:
            if s > last_finish:
                count += 1
                last_finish = f  # Update the last finish time

        return count


#{ 
 # Driver Code Starts
def main():
    t = int(input().strip())  # Number of test cases

    for _ in range(t):
        # Read the start times
        start = list(map(int, input().strip().split()))

        # Read the finish times
        finish = list(map(int, input().strip().split()))

        # Create solution object and call activitySelection
        obj = Solution()
        print(obj.activitySelection(start, finish))
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends