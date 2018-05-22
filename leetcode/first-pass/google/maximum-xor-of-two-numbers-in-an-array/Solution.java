/**
  Used the hint of using a Trie, though still with that I was getting time-out.

  After a lot of failed attempts to optimize, I ported my Python version to Java,
  but still time outs! (this port is also reason for some extra bit operations,
  as Python lacks oob 32-bit integers).

  At last I decided to see the spoiler and realized that my solution was quite
  similar, but a key difference was the usage of an array instead of a HashMap.
  I made that low level optimization and finally passed all tests.

  Rational behind the algorithm:

  The bit-length of the numbers is bounded (<=32), hence we can exploit that
  constant and aim to get a complexity of o(32 * n) ~ O(n).

  First we build a trie with the bit-arrays that the numbers represent, from
  left to right (this order is important cause we will give preference to
  higher order bits).

  Secondly we prune the portion of the Trie where just one branch is available.
  This is just an optimization, and perhaps not that critical; idea is to reduce
  the constant 32 even further, exploting common bit prefixes to all numbers.

  Finally, for each number we explore what is the best possible match; in the
  sense of giving the max XOR. The idea is to search in the Trie, from the root,
  a path that is as similar as possible to the negation of the number (in bits).
  This is because the maximum possible result is all 1's, which could be obtained
  with x ^ ~x. Since is unlikely to have ~x on nums, we search for the closest
  possible.

  Descending the Trie is equivalent to exploring the bits from left to
  right, hence we always give preference to higher order bits. Additionally,
  on each nested iteration lookup first the negated bit, and if not present
  choose the regular bit. These two strategies guarantee that we always pick
  the best match for each number (proof?).

  As we compute the max XOR per number, we also update the global maximum.
**/

class Solution {
    private static class TrieNode {
        public TrieNode[] child;
        public TrieNode() {
            child = new TrieNode[2];
        }
    }

    public int findMaximumXOR(int[] nums) {
        if (nums.length == 0 || nums.length == 1)
            return 0;
        TrieNode root = new TrieNode();
        TrieNode node;
        for(Integer x: nums) {
            node = root;
            for(int i=30; i >= 0; i--) {
                int bit = (x & (1 << i)) >> i;
                if (node.child[bit] == null)
                    node.child[bit] = new TrieNode();
                node = node.child[bit];
            }
        }
        node = root;
        int k = 30;
        while (!(node.child[0] != null && node.child[1] != null)) {
            if (node.child[1] != null)
                node = node.child[1];
            else
                node = node.child[0];
            k -= 1;
        }
        root = node;
        int mask = 0x7fffffff;
        mask = (mask & (mask << (30 - k))) >> (30 - k);
        int maxor = 0;
        for(Integer x: nums) {
            x = mask & x;
            int path = 0;
            node = root;
            for(int i=k; i >= 0; i--) {
                int bit = (x & (1 << i)) >> i;
                int nbit = 1 & ~bit;
                if (node.child[nbit] != null) {
                    node = node.child[nbit];
                    path |= nbit << i;
                } else {
                    node = node.child[bit];
                    path |= bit << i;
                }
            }
            maxor = Math.max(maxor, x ^ path);
        }
        return maxor;
    }
}