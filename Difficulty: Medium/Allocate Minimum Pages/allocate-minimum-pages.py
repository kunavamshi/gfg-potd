class Solution:
    
    # Function to check if a given max_pages can be assigned to students
    def isPossible(self, arr, n, k, max_pages):
        students_required = 1
        current_sum = 0
        
        for pages in arr:
            if pages > max_pages:  # A single book has more pages than max_pages
                return False
            if current_sum + pages > max_pages:
                students_required += 1
                current_sum = pages
                if students_required > k:
                    return False
            else:
                current_sum += pages
        
        return True
    
    # Function to find the minimum number of pages
    def findPages(self, arr, k):
        n = len(arr)
        
        # If books are fewer than students, allocation is not possible
        if n < k:
            return -1
        
        # Binary search boundaries
        low = max(arr)  # At least one book's max pages
        high = sum(arr)  # Sum of all pages
        result = -1
        
        while low <= high:
            mid = (low + high) // 2
            
            if self.isPossible(arr, n, k, mid):
                result = mid  # Update the result as we minimize max_pages
                high = mid - 1  # Look for a smaller maximum
            else:
                low = mid + 1  # Increase max_pages as current mid isn't feasible
        
        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import bisect
#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.findPages(A, D)
        print(ans)
        print("~")

# } Driver Code Ends