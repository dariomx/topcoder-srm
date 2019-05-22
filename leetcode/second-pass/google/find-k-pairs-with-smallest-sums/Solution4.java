import java.util.*;

class Solution {
    public List<int[]> kSmallestPairs(int[] nums1, int[] nums2, int k) {
        PriorityQueue<Tuple> minHeap = new PriorityQueue<>(k);
        for(int i=0; i<Math.min(k, nums1.length); i++)
            for(int j=0; j<Math.min(k, nums2.length); j++) {
                minHeap.add(new Tuple(nums1[i], nums2[j]));
                if ( minHeap.size() > k ) {
                    minHeap.poll();
                }
                System.out.println(minHeap);
            }
        LinkedList<int[]> pairs = new LinkedList<>();
        for(Tuple tup: minHeap) {
            pairs.addFirst(new int[]{tup.x, tup.y});
        }
        return pairs;
    }

    private static class Tuple implements Comparable {
        int x;
        int y;
        public Tuple(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public int compareTo(Object obj) {
            Tuple other = (Tuple) obj;
            int ret = (other.x+other.y) - (this.x+this.y);
            System.out.printf("(%d,%d) cmp (%d,%d) -> %d\n",
                             this.x, this.y, other.x, other.y, ret);
            return ret;
        }

        @Override
        public String toString() {
            return String.format("(%d,%d)", x, y);
        }
    }
}