import java.util.*;
import java.util.function.*;

class Solution {
    private static class Cell implements Comparable<Cell> {
        public int val;
        public int x;
        public int y;

        public Cell(int x, int y, int[][] matrix) {
            this.val = matrix[x][y];
            this.x = x;
            this.y = y;
        }

        @Override
        public boolean equals(Object obj) {
            if ( obj != null && obj instanceof Cell ) {
                Cell other = (Cell) obj;
                return val == other.val &&
                       x == other.x &&
                       y == other.y;
            } else {
                return false;
            }
        }

        @Override
        public int compareTo(Cell other) {
            int cmp = val - other.val;
            if ( cmp == 0 ) {
                cmp = x - other.x;
                if ( cmp == 0 ) {
                    cmp = y - other.y;
                }
            }
            return cmp;
        }

        @Override
        public int hashCode() {
            int hash = 17;
            hash = hash * 31 + val;
            hash = hash * 31 + x;
            hash = hash * 31 + y;
            return hash;
        }

        @Override
        public String toString() {
            return String.format("(%d,%d,%d)", val, x, y);
        }
    }

    public int kthSmallest(int[][] matrix, int k) {
        int n = matrix.length;
        PriorityQueue<Cell> heap = new PriorityQueue<>(n);
        heap.add(new Cell(0, 0, matrix));
        int i = 0;
        Cell cell = null;
        while (i < k) {
            cell = heap.poll();
            i++;
            if (cell.y+1 < n ) {
                Cell right = new Cell(cell.x, cell.y+1, matrix);
                if (!heap.contains(right)) {
                    heap.add(right);
                }
            }
            if (cell.x+1 < n) {
                Cell down = new Cell(cell.x+1, cell.y, matrix);
                if (!heap.contains(down)) {
                    heap.add(down);
                }
            }
        }
        return cell.val;
    }
}