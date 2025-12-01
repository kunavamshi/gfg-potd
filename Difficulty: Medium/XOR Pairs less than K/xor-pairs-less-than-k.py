class Solution:
    def cntPairs(self, arr, k):
        # Binary trie: each node -> {0: child, 1: child, 'cnt': count}
        class TrieNode:
            __slots__ = ("child", "cnt")
            def __init__(self):
                self.child = [None, None]
                self.cnt = 0
        
        root = TrieNode()
        MAX_BIT = 15  # arr[i] <= 5*10^4 < 2^16

        def insert(num):
            node = root
            for b in range(MAX_BIT, -1, -1):
                bit = (num >> b) & 1
                if not node.child[bit]:
                    node.child[bit] = TrieNode()
                node = node.child[bit]
                node.cnt += 1

        def query(num, k):
            node = root
            ans = 0
            for b in range(MAX_BIT, -1, -1):
                if not node:
                    break
                x = (num >> b) & 1
                kb = (k >> b) & 1

                if kb == 1:
                    # add counts from matching branch (XOR=0)
                    if node.child[x]:
                        ans += node.child[x].cnt
                    node = node.child[1-x]  # continue in XOR=1 branch
                else:
                    node = node.child[x]  # forced to XOR=0
            return ans

        count = 0
        for num in arr:
            count += query(num, k)
            insert(num)

        return count