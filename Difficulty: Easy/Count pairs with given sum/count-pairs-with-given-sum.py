#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


# } Driver Code Ends
#User function Template for python3

class Solution:
    # Complete the below function
    def countPairs(self, arr, target):
        count_map = {}
        pair_count = 0

        # Count frequency of each element in the array
        for num in arr:
            count_map[num] = count_map.get(num, 0) + 1

        for num in arr:
            complement = target - num
            if complement in count_map:
                pair_count += count_map[complement]

                # If complement and num are the same, decrease count to avoid double-counting
                if complement == num:
                    pair_count -= 1

        # Each pair is counted twice, so divide by 2
        return pair_count // 2

#{ 
 # Driver Code Starts.

def main():
    T = int(input())
    while (T > 0):

        A = [int(x) for x in input().strip().split()]

        k = int(input())
        ob = Solution()
        print(ob.countPairs(A, k))
        print('~')
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends