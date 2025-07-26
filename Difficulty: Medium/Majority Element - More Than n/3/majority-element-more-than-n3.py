class Solution:
    def findMajority(self, arr):
        if not arr:
            return []
        
        # Step 1: Find up to two candidates
        candidate1, candidate2, count1, count2 = None, None, 0, 0
        
        for num in arr:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
        
        # Step 2: Verify the candidates
        count1 = count2 = 0
        for num in arr:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
        
        result = []
        n = len(arr)
        if count1 > n // 3:
            result.append(candidate1)
        if count2 > n // 3:
            result.append(candidate2)
        
        return sorted(result)