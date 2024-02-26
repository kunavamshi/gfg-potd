#User function Template for python3

class Solution:
	def AllPossibleStrings(self, s):
		# Code here
		# Initialize an empty list to store the subsequences
		subsequences = []
		# Loop through all the possible binary masks of length n
		for mask in range(1, 1 << len(s)):
			# Initialize an empty string to store the current subsequence
			subsequence = ""
			# Loop through the characters of s
			for i in range(len(s)):
				# If the i-th bit of mask is 1, append the i-th character of s to the subsequence
				if mask & (1 << i):
					subsequence += s[i]
			# Append the subsequence to the list
			subsequences.append(subsequence)
		# Sort the list lexicographically
		subsequences.sort()
		# Return the list
		return subsequences

#{ 
 # Driver Code Starts

#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		ob = Solution();
		ans = ob.AllPossibleStrings(s)
		for i in ans:
			print(i, end = " ");
		print()
# } Driver Code Ends