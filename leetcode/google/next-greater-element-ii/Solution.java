import java.util.*;

class Solution {
    private static class Node implements Comparable<Node> {
        public int val;
        public int idx;

        public Node(int val, int idx) {
            this.val = val;
            this.idx = idx;
        }

        @Override
        public int compareTo(Node other) {
            int cmp = this.val - other.val;
            if (cmp == 0) {
                cmp = this.idx - other.idx;
            }
            return cmp;
        }

        @Override
        public boolean equals(Object other) {
            if ( other != null &&  other instanceof Node) {
                return compareTo((Node) other) == 0;
            } else {
                return false;
            }
        }

        public String toString() {
            return String.format("(%d,%d)", this.val, this.idx);
        }
    }

    private void traverse(Node[] nodes,
                          int start,
                          int end,
                          TreeSet<Node> tree,
                          int[] ans) {
        for(int i=start; i<end; i++) {
            //System.out.format("headSet of %s for %s\n", tree, nodes[i]);
            for(Node n: new TreeSet<Node>(tree.headSet(nodes[i]))) {
                //System.out.format("found %s for %s\n", n, nodes[i]);
                if ( nodes[i].val > n.val ) {
                    if (ans[n.idx] < 0) {
                        ans[n.idx] = nodes[i].val;
                    }
                    tree.remove(n);
                }
            }
            tree.add(nodes[i]);
        }
    }

    public int[] nextGreaterElements(int[] nums) {
        int m = nums.length;
        if ( m == 0 ) {
            return nums;
        }
        Node[] nodes =
            IntStream.range(0, m).
            mapToObj(i -> new Node(nums[i], i)).
            toArray(size -> new Node[m]);
        int[] ans = new int[m];
        Arrays.fill(ans, -1);
        TreeSet<Node> tree = new TreeSet();
        tree.add(nodes[0]);
        traverse(nodes, 1, m, tree, ans);
        traverse(nodes, 0, m-1, tree, ans);
        return ans;
    }
}