class TrieNode:
    def __init__(self):
        self.child = dict()


class Solution:
    def findMaximumXOR(self, nums):
        if len(nums) in (0,1):
            return 0
        root = TrieNode()
        for x in nums:
            node = root
            for i in range(30, -1, -1):
                bit = (x & (1 << i)) >> i
                if bit not in node.child:
                    node.child[bit] = TrieNode()
                node = node.child[bit]
        node = root
        k = 30
        while len(node.child) == 1:
            if 1 in node.child:
                node = node.child[1]
            else:
                node = node.child[0]
            k -= 1
        root = node
        mask = 0x7fffffff
        mask = (mask & (mask << (30 - k))) >> (30 - k)
        maxor = 0
        for x in nums:
            x = mask & x
            path = 0
            node = root
            for i in range(k, -1, -1):
                bit = (x & (1 << i)) >> i
                nbit = 1 & ~bit
                if nbit in node.child:
                    node = node.child[nbit]
                    path |= nbit << i
                else:
                    node = node.child[bit]
                    path |= bit << i
            maxor = max(maxor, x ^ path)
        return maxor

