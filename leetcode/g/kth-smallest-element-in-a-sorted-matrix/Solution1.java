import java.util.*;
import java.util.function.*;

class Solution {
    private static class Tuple {
        public int x;
        public int y;

        public Tuple(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public boolean equals(Object obj) {
            if ( obj != null && obj instanceof Tuple ) {
                Tuple other = (Tuple) obj;
                return x == other.x && y == other.y;
            } else {
                return false;
            }
        }

        @Override
        public int hashCode() {
            int hash = 17;
            hash = hash * 31 + x;
            hash = hash * 31 + y;
            return hash;
        }

        @Override
        public String toString() {
            return String.format("(%d,%d)", x, y);
        }
    }

    public int kthSmallest(int[][] matrix, int k) {
        int n = matrix.length;
        Comparator<Tuple> cmp = new Comparator<Tuple>() {
            public int compare(Tuple t1, Tuple t2) {
                int cmp = matrix[t1.x][t1.y] - matrix[t2.x][t2.y];
                if (cmp == 0) {
                    cmp = (t1.x*n + t1.y) - (t2.x*n + t2.y);
                }
                return cmp;
            }
        };
        PriorityQueue<Tuple> heap = new PriorityQueue<>(n, cmp);
        heap.add(new Tuple(0, 0));
        int i = 0;
        Tuple tup = null;
        while (i < k) {
            System.out.println(heap);
            tup = heap.poll();
            i++;
            if (tup.y+1 < n ) {
                tup = new Tuple(tup.x, tup.y+1);
                if (!heap.contains(tup)) {
                    heap.add(tup);
                }
            }
            if (tup.x+1 < n) {
                tup = new Tuple(tup.x+1, tup.y);
                if(!heap.contains(tup)) {
                    heap.add(tup);
                }
            }
        }
        return matrix[tup.x][tup.y];
    }
}