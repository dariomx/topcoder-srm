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

        @Override
        public int compareTo(Node other) {
            int cmp = this.val - other.val;
            if ( cmp == 0 ) {
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
        Comparator<Node> idxCmp = (Node n1, Node n2) -> n1.idx - n2.idx;
        Node key = new Node(0,0);
        for(int i=0; i<m; i++) {
            Node n = nodes.get(i);
            tree.remove(n);
            key.val = n.val + 1;
            SortedSet<Node> tail = tree.tailSet(key, true);
            if ( !tail.isEmpty() ) {
                Node gt = Collections.min(tail, idxCmp);
                ans[n.idx%m] = gt.val;
            }
            n.idx += m;
            tree.add(n);
        }
        return ans;
    }
}