class Solution:
    def countSubstr(self, s, k):
        def atMostK(s, k):
            count = {}
            res = i = 0
            for j in range(len(s)):
                count[s[j]] = count.get(s[j], 0) + 1
                while len(count) > k:
                    count[s[i]] -= 1
                    if count[s[i]] == 0:
                        del count[s[i]]
                    i += 1
                res += j - i + 1
            return res

        return atMostK(s, k) - atMostK(s, k - 1)