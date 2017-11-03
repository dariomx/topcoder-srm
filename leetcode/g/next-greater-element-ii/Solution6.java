import java.util.*;
import java.util.stream.*;

class Solution {
    private static long size;

    private static class Node implements Comparable<Node> {
        public int val;
        public int idx;

        public Node(int val, int idx) {
            this.val = val;
            this.idx = idx;
        }

        private long score() {
            return this.val*Solution.size + this.idx;
        }

        @Override
        public int compareTo(Node other) {
            long myScore = score();
            long otherScore = other.score();
            if ( myScore < otherScore ) {
                return -1;
            } else if ( myScore == otherScore ) {
                return 0;
            } else {
                return 1;
            }

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
        Solution.size = 2*m;
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
            //System.out.format("searching %s in %s = %s\n", key, tree, tail);
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