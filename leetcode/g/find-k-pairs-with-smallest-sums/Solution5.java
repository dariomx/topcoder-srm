import java.util.*;

class Solution {
    public List<int[]> kSmallestPairs(int[] nums1, int[] nums2, int k) {
        TreeSet<Tuple> tree = new TreeSet<>();
        for(int i=0; i<Math.min(k, nums1.length); i++)
            for(int j=0; j<Math.min(k, nums2.length); j++) {
                tree.add(new Tuple(nums1[i], i, nums2[j], j));
                if ( tree.size() > k ) {
                    tree.pollLast();
                }
            }
        List<int[]> pairs = new ArrayList<>();
        for(Tuple tup: tree) {
            pairs.add(new int[]{tup.x, tup.y});
        }
        return pairs;
    }

    private static class Tuple implements Comparable {
        int x;
        int i;
        int y;
        int j;
        public Tuple(int x, int i, int y, int j) {
            this.x = x;
            this.i = i;
            this.y = y;
            this.j = j;
        }

        @Override
        public int compareTo(Object obj) {
            Tuple other = (Tuple) obj;
            int cmp = (this.x+this.y) - (other.x+other.y);
            if ( cmp == 0 ) {
                cmp = this.i - other.i;
                if ( cmp == 0 ) {
                    cmp = this.j - other.j;
                }
            }
            return cmp;
        }

        public boolean equals(Object other) {
            return compareTo(other) == 0;
        }

        @Override
        public String toString() {
            return String.format("([%d,%d], [%d,%d])", x,i, y,j);
        }
    }
}