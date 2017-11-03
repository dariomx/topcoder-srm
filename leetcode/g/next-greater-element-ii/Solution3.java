import java.util.*;
import java.util.stream.*;

class Solution {
    private static class Node implements Comparable<Node> {
        public int val;
        public int idx;

        public Node(int val, int idx) {
            this.val = val;
            this.idx = idx;
        }

        private int score() {
            return this.val*10000 + this.idx;
        }

        @Override
        public int compareTo(Node other) {
            return this.score() - other.score();
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
            return String.format("(%d,%d,%d)", this.val, this.idx, this.score());
        }
    }

    public int[] nextGreaterElements(int[] nums) {
        int m = nums.length;
        if ( m == 0 ) {
            return nums;
        }
        List<Node> nodes =
            IntStream.range(0, m).
            mapToObj(i -> new Node(nums[i], i)).
            collect(Collectors.toList());
        int[] ans = new int[m];
        Arrays.fill(ans, -1);
        TreeSet<Node> tree = new TreeSet(nodes);
        Node key = new Node(0,0);
        for(int i=0; i<m; i++) {
            Node n = nodes.get(i);
            tree.remove(n);
            key.val = n.val + 1;
            Node gt = tree.ceiling(key);
            System.out.format("searching %s in %s = %s\n", key, tree, gt);
            if ( gt != null ) {
                ans[n.idx] = gt.val;
            }
            n.idx += m;
            tree.add(n);
        }
        return ans;
    }
}